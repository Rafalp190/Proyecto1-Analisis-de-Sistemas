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
        db_table = 'invetario'
 
#idproducto, id platillo, cantidad utilizada, idingrediente
class Ingredientes (models.Model):
    idPlatillo = models.BigIntegerField(primary_key=True,verbose_name='Id Platillo')
    idProducto = models.BigIntegerField(db_column='idProducto',blank=True,verbose_name='Id Producto')
    cantidadUtilizada = models.BigIntegerField(db_column='cantidadUtilizada',blank=True,verbose_name='Cantidad')
    idIngrediente = models.BigIntegerField(db_column='idIngrediente',blank=True,verbose_name='Id Ingrediente')
     
 
    class Meta:
        managed = True
        db_table = 'ingredientes'
 
#cliente, nit, id platillo, id mesero
class Ordenes (models.Model):
   cliente = models.CharField(max_length=255, primary_key=True, verbose_name = 'Cliente')
   nit = models.BigIntegerField (db_column = 'nit',blank = True, verbose_name= 'Nit')
   idPlatillo = models.BigIntegerField(db_column='idPlatillo',blank=True,verbose_name='Id Platillo')
   idMesero= models.BigIntegerField (db_column='idMesero',blank=True,verbose_name='Id Mesero')
   class Meta:
        managed = True
#         db_table = 'orden'