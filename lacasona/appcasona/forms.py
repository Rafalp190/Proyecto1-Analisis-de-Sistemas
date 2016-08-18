    
from django import forms
from .models import Inventario,Ingredientes,Orders
from crispy_forms.helper import FormHelper

class InventarioFormHelper(FormHelper):
    model = Inventario
    form_tag = False

class IngredientesFormHelper(FormHelper):
    model = Ingredientes
    form_tag = False
    
class OrdenesFormHelper(FormHelper):
    model = Orders
    form_tag = False