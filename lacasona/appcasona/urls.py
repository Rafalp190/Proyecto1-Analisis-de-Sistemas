from django.conf.urls import patterns, url
from appcasona import views

urlpatterns = [
               url(r'^$', views.log_in, name='login'),
               url(r'^init/', views.log_out, name='logout'),
               url(r'^index/', views.index, name='index'),
               url(r'^inventory/', views.inventory, name='inventory')
               ]