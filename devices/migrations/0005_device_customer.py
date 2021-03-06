# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '0004_device_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_devices', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
