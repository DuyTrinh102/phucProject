# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_device_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]
