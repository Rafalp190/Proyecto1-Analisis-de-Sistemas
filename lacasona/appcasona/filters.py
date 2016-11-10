import django_filters as df
from .models import Inventario, Platillo, Orden

class InventarioFilter(df.FilterSet):
    class Meta:
        model = Inventario
        fields = ['id', 'nombreDelProducto','cantidadDeProducto','seccion','proveedor']
        
        
# class ProveedorFilter(df.FilterSet):
#     class Meta:
#         model = Proveedor
#         fields = ['idProveedor', 'nombreDelProveedor','numeroDelProveedor','direccionDelProveedor']

class PlatilloFilter(df.FilterSet):
    class Meta:
        model = Platillo
        fields = ['id', 'nombreDelPlatillo', 'precioPlatillo','imagenPlatillo','ingredientes', 'descripcionPlatillo']

class OrdenFilter(df.FilterSet):
	class Meta: 
		model = Orden
		fields = ['id', 'nombreDelMesero', 'precioPlatillo', 'cantidad', 'mesa', 'fecha']