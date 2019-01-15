# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Measurement(models.Model):
	value = models.FloatField(default=0)
	receive_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'value:{} at {}'.format(self.value, self.receive_at.strftime("%Y/%m/%d-%H:%M"))


class Device(models.Model):
	customer = models.ForeignKey(User, related_name="related_devices")
	serial = models.CharField(max_length=50, unique=True)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200, blank=True, null=True)
	unit = models.CharField(max_length=50)
	measure = models.ManyToManyField(Measurement, related_name="measure_device", blank=True)
