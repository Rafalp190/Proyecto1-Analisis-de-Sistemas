import django_filters as df
from .models import Inventario, Ingredientes,Orders

class InventarioFilter(df.FilterSet):
    class Meta:
        model = Inventario
        fields = ['idProducto', 'nombreDelProducto']
        
        
class IngredientesFilter(df.FilterSet):
    class Meta:
        model = Ingredientes
        fields = ['idIngrediente', 'nombreDelProducto']

class OrdenesFilter(df.FilterSet):
    class Meta:
        model = Orders
        fields = ['factura', 'cliente', 'nit']