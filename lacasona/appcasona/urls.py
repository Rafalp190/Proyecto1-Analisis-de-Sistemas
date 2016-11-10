from django.conf.urls import url
from appcasona import views
from django.views.generic.base import RedirectView


urlpatterns = [
               url(r'^$', views.log_in, name='login'),
               url(r'^init/', views.log_out, name='logout'),
               url(r'^index/', views.index, name='index'),
               url(r'^menu/', views.menu, name='menu'),
               url(r'^inventory/', RedirectView.as_view(url="/admin/appcasona/inventario/"), name='inventory'),
               #url(r'^proveedor/', RedirectView.as_view(url="/admin/appcasona/proveedor/"), name='proveedor'),
               url(r'^platillo/', RedirectView.as_view(url="/admin/appcasona/platillo/"), name='platillo'),
               url(r'^orden/', RedirectView.as_view(url="/admin/appcasona/orden/"), name='orden')
               ]