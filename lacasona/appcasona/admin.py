from django.contrib import admin

# Register your models here.
from models import Inventario, Platillo, Orden


# class ProveedorAdmin(admin.ModelAdmin):
#     list_display = ('idProveedor', 'nombreDelProveedor', 'numeroDelProveedor')
#     search_fields = ('idProveedor', 'nombreDelProveedor', 'numeroDelProveedor')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreDelProducto', 'cantidadDeProducto', 'seccion')
    search_fields = ('id', 'nombreDelProducto', 'seccion')

class PlatilloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreDelPlatillo', 'precioPlatillo', 'descripcionPlatillo', )
    search_fields = ('id', 'nombreDelPlatillo', 'precioPlatillo', 'descripcionPlatillo', )

class OrdenAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreDelMesero', 'mesa', 'fecha', 'status')
	search_fields = ('id', 'nombreDelMesero', 'mesa', 'fecha', 'status')

#admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Platillo, PlatilloAdmin)
admin.site.register(Orden, OrdenAdmin)
