    
from django import forms
from .models import Inventario, Proveedor, Platillo, Orden
from crispy_forms.helper import FormHelper

class InventarioFormHelper(FormHelper):
    model = Inventario
    form_tag = False

class ProveedorFormHelper(FormHelper):
    model = Proveedor
    form_tag = False
    
class PlatilloFormHelper(FormHelper):
    model = Platillo
    form_tag = False

class OrdenFormHelper(FormHelper):
    model = Orden
    form_tag = False