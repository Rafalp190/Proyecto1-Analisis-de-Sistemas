import django_filters as df
from .models import Inventario, Ingredientes, Orden

class InventarioFilter(df.FilterSet):
    class Meta:
        model = Inventario
        fields = ['idProducto', 'nombreDelProducto']