from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.'
 
#idproducto, cantidad de producto, nombre del producto 
class Inventario (models.Model):
    idProducto = models.BigIntegerField(primary_key=True,verbose_name='ID')
    cantidadDeProducto = models.BigIntegerField(db_column='cantidadDeProducto',blank=True,verbose_name='Cantidad')
    nombreDelProducto = models.CharField(max_length=255, blank=True,verbose_name='Nombre',db_column='nombreDelProducto')
     
    class Meta:
        managed = True
        db_table = 'inventario'
 
#idproducto, id platillo, cantidad utilizada, idingrediente
class Ingredientes (models.Model):
    idIngrediente = models.BigIntegerField(primary_key=True,verbose_name='ID')
    nombreDelProducto = models.CharField(max_length=255, blank=True,verbose_name='Nombre',db_column='nombreDelProducto')
    idPlatillo = models.BigIntegerField(db_column='idPlatillo',verbose_name='Id Platillo')
    idProducto = models.BigIntegerField(db_column='idProducto',blank=True,verbose_name='Id Producto')
    cantidadUtilizada = models.BigIntegerField(db_column='cantidadUtilizada',blank=True,verbose_name='Cantidad')
     
 
    class Meta:
        managed = True
        db_table = 'ingrediente'
 
#cliente, nit, id platillo, id mesero
class Orders (models.Model):
    cliente = models.CharField(max_length=255, db_column = 'cliente', verbose_name = 'Cliente')
    nit = models.BigIntegerField (db_column = 'nit',blank = True, verbose_name= 'Nit')
    factura = models.BigIntegerField (primary_key=True, blank = True, verbose_name= 'Factura')
    idPlatillo = models.BigIntegerField(db_column='idPlatillo',blank=True,verbose_name='Id Platillo')
    idMesero= models.BigIntegerField (db_column='idMesero',blank=True,verbose_name='Id Mesero')
    class Meta:
        managed = True
        db_table = 'ordenes'
        