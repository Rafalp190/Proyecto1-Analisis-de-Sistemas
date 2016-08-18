import django_filters as df
from .models import Inventario, Ingredientes, Ordenes

class InventarioFilter(df.FilterSet):
    class Meta:
        model = Inventario
        fields = ['idProducto', 'nombreDelProducto']