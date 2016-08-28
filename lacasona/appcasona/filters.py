import django_filters as df
from .models import Inventario, Proveedor,Platillo

class InventarioFilter(df.FilterSet):
    class Meta:
        model = Inventario
        fields = ['idProducto', 'nombreDelProducto','cantidadDeProducto','seccion','proveedor']
        
        
class ProveedorFilter(df.FilterSet):
    class Meta:
        model = Proveedor
        fields = ['idProveedor', 'nombreDelProveedor','numeroDelProveedor','direccionDelProveedor']

class PlatilloFilter(df.FilterSet):
    class Meta:
        model = Platillo
        fields = ['idPlatillo', 'nombreDelPlatillo', 'precioPlatillo','imagenPlatillo','ingredientes']