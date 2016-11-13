from django.contrib import admin

# Register your models here.
from models import Inventario, Platillo, Orden, Cantidad


# class ProveedorAdmin(admin.ModelAdmin):
#     list_display = ('idProveedor', 'nombreDelProveedor', 'numeroDelProveedor')
#     search_fields = ('idProveedor', 'nombreDelProveedor', 'numeroDelProveedor')

class CantidadInline(admin.TabularInline):
    model = Cantidad
    extra = 1

class InventarioAdmin(admin.ModelAdmin):
    inlines = (CantidadInline,)

class PlatilloAdmin(admin.ModelAdmin):
    inlines = (CantidadInline,)



class OrdenAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreDelMesero', 'mesa', 'fecha', 'status')
	search_fields = ('id', 'nombreDelMesero', 'mesa', 'fecha', 'status')

#admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Platillo, PlatilloAdmin)
admin.site.register(Orden, OrdenAdmin)
