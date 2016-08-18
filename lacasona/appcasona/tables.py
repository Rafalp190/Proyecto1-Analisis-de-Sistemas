import django_tables2 as dt2
import itertools
from datetime import datetime
from .models import Message
from django import forms
from django.utils.html import escape

class Ingredientes (dt2.Table):
    idPlatillo = dt2.Column(accessor='id')
    idProducto = dt2.Column(accessor='idProducto')
    cantidadUtilizada = dt2.Column(accessor='cantidadUtilizada')
    idIngrediente = dt2.Column(accessor='idIngrediente')
    
class Inventario (dt2.Table):
    idProducto = dt2.Column(accessor='id')
    cantidadDeProducto = dt2.Column(accessor='cantidadDeProducto')
    nombreDelProducto = dt2.Column(accessor='nombreDelProducto')
    
class Ordenes (dt2.Table):
   cliente = dt2.Column(accessor='id')
   nit = dt2.Column(accessor= 'nit')
   idPlatillo = dt2.Column(accessor='idPlatillo')
   idMesero= dt2.Column(accessor='idMesero')