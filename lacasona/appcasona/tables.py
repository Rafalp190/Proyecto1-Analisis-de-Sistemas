import django_tables2 as dt2
import itertools
from datetime import datetime
from .models import Inventario
from django import forms
from django.utils.html import escape

class IngredientesTable (dt2.Table):
    idPlatillo = dt2.Column(accessor='id')
    idProducto = dt2.Column(accessor='idProducto')
    cantidadUtilizada = dt2.Column(accessor='cantidadUtilizada')
    idIngrediente = dt2.Column(accessor='idIngrediente')
    
class InventarioTable (dt2.Table):
    model = Inventario
    idProducto = dt2.Column(accessor='id')
    cantidadDeProducto = dt2.Column(accessor='cantidadDeProducto')
    nombreDelProducto = dt2.Column(accessor='nombreDelProducto')
    
class OrdenesTable (dt2.Table):
   cliente = dt2.Column(accessor='id')
   nit = dt2.Column(accessor= 'nit')
   idPlatillo = dt2.Column(accessor='idPlatillo')
   idMesero= dt2.Column(accessor='idMesero')