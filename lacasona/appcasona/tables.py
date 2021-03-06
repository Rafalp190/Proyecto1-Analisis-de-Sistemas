import django_tables2 as dt2
import itertools
from datetime import datetime
from .models import Inventario
from django import forms
from django.utils.html import escape


class InventarioTable(dt2.Table):
    idProducto = dt2.Column(accessor='id')
    nombreDelProducto = dt2.Column(accessor='nombreDelProducto')
    cantidadDeProducto = dt2.Column(accessor='cantidadDeProducto')
    seccion = dt2.Column(accessor='seccion')
    proveedor = dt2.Column(accessor='proveedor')

    def __init__(self, *args, **kwargs):
        super(InventarioTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()


# class ProveedorTable(dt2.Table):
#     idProveedor = dt2.Column(accessor='idProveedor')
#     nombreDelProveedor = dt2.Column(accessor='nombreDelProveedor')
#     numeroDelProveedor = dt2.Column(accessor='numeroDelProveedor')
#     direccionDelProveedor = dt2.Column(accessor='direccionDelProveedor')
#
#     def __init__(self, *args, **kwargs):
#         super(ProveedorTable, self).__init__(*args, **kwargs)
#         self.counter = itertools.count()


class PlatilloTable(dt2.Table):
    idPlatillo = dt2.Column(accessor='id')
    nombreDelPlatillo = dt2.Column(accessor='nombreDelPlatillo')
    precioPlatillo = dt2.Column(accessor='precioPlatillo')
    imagenPlatillo = dt2.Column(accessor='imagenPlatillo')
    ingredientes = dt2.Column(accessor='ingredientes')
    descripcionPlatillo = dt2.Column(accessor='descripcionPlatillo')

    def __init__(self, *args, **kwargs):
        super(PlatilloTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()


class OrdenTable(dt2.Table):
    ordenNo = dt2.Column(accessor='id')
    nombreDelMesero = dt2.Column(accessor='nombreDelMesero')
    precioPlatillo = dt2.Column(accessor='precioPlatillo')
    cantidad = dt2.Column(accessor='cantidad')
    mesa = dt2.Column(accessor='mesa')
    fecha = dt2.Column(accessor='fecha')
    platillos = dt2.Column(accessor='platillos')


    def __init__(self, *args, **kwargs):
        super(OrdenTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()