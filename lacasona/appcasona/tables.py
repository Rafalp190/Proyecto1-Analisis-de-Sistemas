from __future__ import unicode_literals

from django.db import models

# Create your models here.'

# #idproducto, cantidad de producto
# class Inventario (models.Model):
#     idProducto = models.BigIntegerField(primary_key=True)
#     content = models.CharField(max_length=255, blank=True)
#     date = models.BigIntegerField(blank=True, null=True)
#     recipients = models.CharField(max_length=255, blank=True)
#     status = models.IntegerField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True)
#     sender = models.ForeignKey('Emailaccount', blank=True, null=True)
#     class Meta:
#         managed = True
#         db_table = 'invetario'
# 
# #idproducto, id platillo, cantidad utilizada, idingrediente
# class Ingredientes (models.Model):
#     idProducto = models.BigIntegerField(primary_key=True)
#     content = models.CharField(max_length=255, blank=True)
#     date = models.BigIntegerField(blank=True, null=True)
#     recipients = models.CharField(max_length=255, blank=True)
#     status = models.IntegerField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True)
#     sender = models.ForeignKey('Emailaccount', blank=True, null=True)
# 
#     class Meta:
#         managed = True
#         db_table = 'ingredientes'
# 
# #cliente, nit, id platillo, id mesero
# class Orden (models.Model):
#     idPlatillo = models.BigIntegerField(primary_key=True)
#     content = models.CharField(max_length=255, blank=True)
#     date = models.BigIntegerField(blank=True, null=True)
#     recipients = models.CharField(max_length=255, blank=True)
#     status = models.IntegerField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True)
#     sender = models.ForeignKey('Emailaccount', blank=True, null=True)
# 
#     class Meta:
#         managed = True
#         db_table = 'orden'