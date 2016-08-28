import django_filters as df
from .models import Inventario, Proveedor,Platillo

class InventarioFilter(df.FilterSet):
    class Meta:
        model = Inventario
        fields = ['idProducto', 'nombreDelProducto']
        
        
class ProveedorFilter(df.FilterSet):
    class Meta:
        model = Proveedor
        fields = ['idIngrediente', 'nombreDelProducto']

class PlatilloFilter(df.FilterSet):
    class Meta:
        model = Platillo
        fields = ['factura', 'cliente', 'nit']