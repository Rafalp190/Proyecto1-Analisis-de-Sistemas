import django_tables2 as dt2
import itertools
from datetime import datetime
from .models import Inventario
from django import forms
from django.utils.html import escape

class IngredientesTable (dt2.Table):
    idIngrediente = dt2.Column(accessor='idIngrediente')
    nombreDelProducto = dt2.Column(accessor='nombreDelProducto')
    cantidadUtilizada = dt2.Column(accessor='cantidadUtilizada')
    idPlatillo = dt2.Column(accessor='idPlatillo')
    idProducto = dt2.Column(accessor='idProducto')
    def __init__(self, *args, **kwargs):
        super(IngredientesTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()
    
class InventarioTable (dt2.Table):
    idProducto = dt2.Column(accessor='idProducto')
    cantidadDeProducto = dt2.Column(accessor='cantidadDeProducto')
    nombreDelProducto = dt2.Column(accessor='nombreDelProducto')
    def __init__(self, *args, **kwargs):
        super(InventarioTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

class OrdenesTable (dt2.Table):
    factura = dt2.Column(accessor= 'factura')
    cliente = dt2.Column(accessor='cliente')
    nit = dt2.Column(accessor= 'nit')
    idPlatillo = dt2.Column(accessor='idPlatillo')
    idMesero= dt2.Column(accessor='idMesero')
    def __init__(self, *args, **kwargs):
        super(OrdenesTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()