# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import partial

from django.db import IntegrityError
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout, authenticate
from .utils import user_detail, generate_number
from devices.models import Device, Measurement


@api_view(['POST'])
@permission_classes((permissions.BasePermission,))
def api_sign_in(request):
	username = request.data.get('username', None)
	password = request.data.get('password', None)
	user = authenticate(username=username, password=password)
	if user:
		token = user_detail(user)
		login(request, user)
		return Response({"result": True, "message": "Successful", "data": [token]}, status=status.HTTP_200_OK)
	return Response({"result": False, "message": "Username or password is wrong", "data": []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def api_device_add(request):
	serial = request.data.get('serial', '')
	name = request.data.get('name', '')
	unit = request.data.get('unit', '')
	description = request.data.get('description', '')
	error = []
	if not serial:
		error.append({
			"field": "serial",
			"message": "Serial is required"
		})
	elif not serial.isalnum():
		error.append({
			"field": "serial",
			"message": "Serial is invalid"
		})
	if not name:
		name = request.user.username + '-{}'.format(generate_number(size=5))
	if not unit:
		error.append({
			"field": "unit",
			"message": "Unit is required"
		})
	if not error:
		try:
			device = Device.objects.create(serial=serial, name=name, unit=unit, description=description, customer=request.user)
			return Response({"result": True, "message": "Successful", "data": [{"device_id": device.id}]}, status=status.HTTP_200_OK)
		except IntegrityError:
			error.append({
				"field": "serial",
				"message": "This device is existed"
			})
	return Response({"result": False, "message": "Error!!!", "data": error}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def api_device_measure_list(request):
	serial = request.data.get('serial', '')
	error = []
	if not serial:
		error.append({
			"field": "serial",
			"message": "Serial is required"
		})
	elif not serial.isalnum():
		error.append({
			"field": "serial",
			"message": "Serial is invalid"
		})

	if not error:
		try:
			device = Device.objects.get(serial=serial, customer=request.user)
			data = device.measure.all().values('value', 'receive_at')
			for temp in data:
				temp['receive_at'] = temp['receive_at'].strftime("%Y-%m-%d %H:%M")
			return Response({"result": True, "message": "Successful", "data": data}, status=status.HTTP_200_OK)
		except Device.DoesNotExist:
			error.append({
				"field": "serial",
				"message": "This device is not existed"
			})
	return Response({"result": False, "message": "Error!!!", "data": error}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def api_device_measure_update(request):
	serial = request.data.get('serial', '')
	value = request.data.get('value', '')
	error = []

	if not serial:
		error.append({
			"field": "serial",
			"message": "Serial is required"
		})
	elif not serial.isalnum():
		error.append({
			"field": "serial",
			"message": "Serial is invalid"
		})
	if not value:
		error.append({
			"field": "value",
			"message": "required"
		})

	if not error:
		try:
			device = request.user.related_devices.get(serial=serial)
		except Device.DoesNotExist:
			error.append({
				"field": "serial",
				"message": "Invalid"
			})
		else:
			measure = Measurement.objects.create(value=value)
			device.measure.add(measure)
			return Response({"result": True, "message": "Successful", "data": []}, status=status.HTTP_200_OK)
	return Response({"result": False, "message": "Error!!!", "data": error}, status=status.HTTP_200_OK)
