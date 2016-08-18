    
from django import forms
from .models import Inventario,Ingredientes,Ordenes
from crispy_forms.helper import FormHelper

class InventarioFormHelper(FormHelper):
    model = Inventario
    form_tag = False