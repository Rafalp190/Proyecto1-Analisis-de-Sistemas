# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcasona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='inventario',
            table='inventario',
        ),
        migrations.AlterModelTable(
            name='ordenes',
            table='orden',
        ),
    ]
