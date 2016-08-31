# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('idProducto', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDelProducto', models.CharField(blank=True, db_column='nombreDelProducto', max_length=255, verbose_name='Nombre')),
                ('cantidadDeProducto', models.BigIntegerField(blank=True, db_column='cantidadDeProducto', verbose_name='Cantidad')),
                ('seccion', models.CharField(blank=True, db_column='Seccion', max_length=255, verbose_name='Seccion')),
            ],
            options={
                'db_table': 'inventario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('idPlatillo', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDelPlatillo', models.CharField(db_column='NombreDelPlatillo', max_length=255, verbose_name='Nombre')),
                ('precioPlatillo', models.BigIntegerField(blank=True, db_column='PrecioDelPlatillo', verbose_name='precio')),
                ('imagenPlatillo', models.CharField(db_column='ImagenPlatillo', max_length=255, verbose_name='Imagen')),
                ('ingredientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcasona.Inventario')),
            ],
            options={
                'db_table': 'platillo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDelProveedor', models.CharField(blank=True, db_column='nombreDelProveedor', default='', max_length=255, verbose_name='Nombre')),
                ('numeroDelProveedor', models.BigIntegerField(db_column='numeroDelProveedor', default=0, verbose_name='Numero')),
                ('direccionDelProveedor', models.CharField(db_column='direccionDelProveedor', default='', max_length=255, verbose_name='Direccion')),
            ],
            options={
                'db_table': 'proveedor',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='inventario',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcasona.Proveedor'),
        ),
    ]