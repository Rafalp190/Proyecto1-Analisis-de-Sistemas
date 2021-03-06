from django.conf.urls import url
from appcasona import views
from django.views.generic.base import RedirectView


urlpatterns = [
               url(r'^$', views.log_in, name='login'),
               url(r'^init/', views.log_out, name='logout'),
               url(r'^index/', views.index, name='index'),
               url(r'^menu/', views.menu, name='menu'),
               url(r'^cocina/', views.cocina, name='cocina'),
               url(r'^caja/', views.caja, name='caja'),
               url(r'^carrito/', views.carrito, name='carrito'),
               url(r'^pagos/', views.pagos, name='pagos'),
               url(r'^inventory/', RedirectView.as_view(url="/admin/appcasona/inventario/"), name='inventory'),
               #url(r'^proveedor/', RedirectView.as_view(url="/admin/appcasona/proveedor/"), name='proveedor'),
               url(r'^(?P<platillo_id>[0-9]+)/descripcion/$', views.platillo_detail, name='descripcion'),
               url(r'^platillo/', RedirectView.as_view(url="/admin/appcasona/platillo/"), name='platillo'),
               url(r'^orden/', RedirectView.as_view(url="/admin/appcasona/orden/"), name='orden'),
               url(r'^(?P<platillo_id>[0-9]+)/otro/$', views.ordenar, name='other')
               ]
