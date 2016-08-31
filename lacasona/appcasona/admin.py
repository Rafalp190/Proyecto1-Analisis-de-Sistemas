from django.contrib import admin

# Register your models here.
from models import Proveedor, Inventario, Platillo


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('idProveedor', 'nombreDelProveedor', 'numeroDelProveedor')
    search_fields = ('idProveedor', 'nombreDelProveedor', 'numeroDelProveedor')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('idProducto', 'nombreDelProducto', 'cantidadDeProducto', 'seccion', )
    search_fields = ('idProducto', 'nombreDelProducto', 'seccion',)

class PlatilloAdmin(admin.ModelAdmin):
    list_display = ('idPlatillo', 'nombreDelPlatillo', 'precioPlatillo', 'descripcionPlatillo', )
    search_fields = ('idPlatillo', 'nombreDelPlatillo', 'precioPlatillo', 'descripcionPlatillo', )

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Platillo, PlatilloAdmin)
