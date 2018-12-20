# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='measure',
            field=models.ManyToManyField(related_name='measure_device', to='devices.Measurement'),
        ),
    ]
