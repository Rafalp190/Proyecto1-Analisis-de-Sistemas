from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.'
#
class Proveedor(models.Model):
    idProveedor = models.BigIntegerField(primary_key=True, verbose_name='ID')
    nombreDelProveedor = models.CharField(max_length=255, blank=True, verbose_name='Nombre',db_column='nombreDelProveedor',default='')
    numeroDelProveedor = models.BigIntegerField(db_column='numeroDelProveedor', verbose_name='Numero',default=0)
    direccionDelProveedor = models.CharField(max_length=255, db_column='direccionDelProveedor', verbose_name='Direccion',default='')

    class Meta:
        managed = True
        db_table = 'proveedor'

    def __unicode__(self):
        return self.nombreDelProveedor

#
class Inventario(models.Model):
    idProducto = models.BigIntegerField(primary_key=True, verbose_name='ID')
    nombreDelProducto = models.CharField(max_length=255, blank=True, verbose_name='Nombre', db_column='nombreDelProducto')
    cantidadDeProducto = models.BigIntegerField(db_column='cantidadDeProducto', blank=True, verbose_name='Cantidad')
    seccion = models.CharField(max_length=255, blank=True, verbose_name='Seccion', db_column='Seccion')
    proveedor = models.ManyToManyField(Proveedor)


    class Meta:
        managed = True
        db_table = 'inventario'

    def __unicode__(self):
        return self.nombreDelProducto



#
class Platillo(models.Model):
    idPlatillo = models.BigIntegerField(primary_key=True, verbose_name='ID')
    nombreDelPlatillo = models.CharField(max_length=255, db_column='NombreDelPlatillo', verbose_name='Nombre')
    precioPlatillo = models.BigIntegerField(db_column='PrecioDelPlatillo', blank=True, verbose_name='precio')
    imagenPlatillo = models.CharField(max_length=255, db_column='ImagenPlatillo', verbose_name='Imagen')
    descripcionPlatillo = models.CharField(max_length=255, db_column='DescripcionDelPlatillo', verbose_name='Descripcion')
    ingredientes = models.ManyToManyField(Inventario)

    class Meta:
        managed = True
        db_table = 'platillo'


    def __unicode__(self):
        return self.nombreDelPlatillo