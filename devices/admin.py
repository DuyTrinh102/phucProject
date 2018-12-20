# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Device, Measurement


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
	list_display = ('serial', 'name', 'description', 'unit', 'customer')
	filter_horizontal = ('measure',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
	list_display = ('value', 'receive_at')
