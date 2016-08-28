from django.conf.urls import url
from appcasona import views

urlpatterns = [
               url(r'^$', views.log_in, name='login'),
               url(r'^init/', views.log_out, name='logout'),
               url(r'^index/', views.index, name='index'),
               url(r'^inventory/', views.Inventory.as_view(), name='inventory'),
               url(r'^proveedor/', views.Proveedor.as_view(), name='proveedor'),
               url(r'^platillo/', views.Platillo.as_view(), name='platillo')
               ]