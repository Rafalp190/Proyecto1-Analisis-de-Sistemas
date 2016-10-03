# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcasona', '0002_auto_20160828_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='disponible',
            field=models.CharField(choices=[('H', 'Habilitado'), ('I', 'Inhabilitado')], db_column='disponible', default='H', max_length=1, verbose_name='disponible'),
        ),
    ]
