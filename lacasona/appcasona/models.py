from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.'
#
# class Proveedor(models.Model):
#     def number():
#         no = models.objects.count()
#         if no == None:
#             return 1
#     else:
#         return no +1
#     idProveedor = models.BigIntegerField(primary_key=True, verbose_name='ID', default=number)
#     nombreDelProveedor = models.CharField(max_length=255, blank=True, verbose_name='Nombre',db_column='nombreDelProveedor',default='')
#     numeroDelProveedor = models.BigIntegerField(db_column='numeroDelProveedor', verbose_name='Numero',default=0)
#     direccionDelProveedor = models.CharField(max_length=255, db_column='direccionDelProveedor', verbose_name='Direccion',default='')
#
#     class Meta:
#         managed = True
#         db_table = 'proveedor'
#
#     def __unicode__(self):
#         return self.nombreDelProveedor

#
class Inventario(models.Model):

    nombreDelProducto = models.CharField(max_length=255, blank=True, verbose_name='Nombre', db_column='nombreDelProducto')
    cantidadDeProducto = models.IntegerField(db_column='cantidadDeProducto', blank=True, verbose_name='Cantidad')
    seccion = models.CharField(max_length=255, blank=True, verbose_name='Seccion', db_column='Seccion')

    def inventario_id(self):
        return self.id

    class Meta:
        managed = True
        db_table = 'inventario'

    def __unicode__(self):
        return self.nombreDelProducto



#
class Platillo(models.Model):
    nombreDelPlatillo = models.CharField(max_length=255, db_column='NombreDelPlatillo', verbose_name='Nombre')
    precioPlatillo = models.FloatField(db_column='PrecioDelPlatillo', blank=True, verbose_name='precio')
    imagenPlatillo = models.CharField(max_length=255, db_column='ImagenPlatillo', verbose_name='Imagen')
    descripcionPlatillo = models.CharField(max_length=255, blank=True, db_column='DescripcionDelPlatillo', verbose_name='Descripcion')
    ingredientes = models.ManyToManyField(Inventario, through='Cantidad')

    def platillo_id(self):
        return self.id

    class Meta:
        managed = True
        db_table = 'platillo'


    def __unicode__(self):
        return self.nombreDelPlatillo


class Cantidad(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.FloatField(db_column='Cantidad', blank=True, verbose_name='cantidad')




class Orden(models.Model):

    nombreDelMesero = models.CharField(max_length=255, db_column='NombreDelMesero', verbose_name='nombreDelMesero')
    mesa = models.IntegerField(blank=True, db_column='Mesa', verbose_name='mesa')
    fecha = models.DateTimeField(max_length=255, db_column='Fecha', verbose_name='fecha')
    status = models.IntegerField(default=0, db_column="Estado", verbose_name="Estado")
    platillos = models.ManyToManyField(Platillo)

    def orden_id(self):
        return self.id

    class Meta:
        managed = True
        db_table = 'ordenes'

    def __int__(self):
        return self.id
