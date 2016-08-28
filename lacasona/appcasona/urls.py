from django.conf.urls import patterns, url
from appcasona import views

urlpatterns = [
               url(r'^$', views.log_in, name='login'),
               url(r'^init/', views.log_out, name='logout'),
               url(r'^index/', views.index, name='index'),
               url(r'^inventory/', views.Inventory.as_view(), name='inventory'),
               url(r'^proveedores/', views.Ingredients.as_view(), name='proveedores'),
               url(r'^platillos/', views.Orders.as_view(), name='platillos')
               ]