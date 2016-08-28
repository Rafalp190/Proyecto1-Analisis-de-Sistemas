#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django_tables2 import SingleTableView

from django.http import HttpResponse
from .models import Inventario,Proveedor,Platillo
from .tables import InventarioTable,ProveedorTable,PlatilloTable
from .filters import InventarioFilter, ProveedorFilter, PlatilloFilter
from .forms import InventarioFormHelper, ProveedorFormHelper, PlatilloFormHelper
from utils import PagedFilteredTableView

import random
import datetime
import time
# Create your views here.
def log_in(request):
    #Maneja los errores
    def errorHandle(error):
        return render(request, 'appcasona/login_template.html', {'error' : error,})
    #Si el usuario no ha iniciado sesion.
    if not request.user.is_authenticated():
        #Si ya se ha dado ingresado una cuenta
        if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    #Redirige a la pagina correcta.
                    login(request, user)
                    return render(request, 'appcasona/index.html', {'user': user,})
                else:
                    #Retorna un mensaje de error de 'disable account'
                    error = u'Su cuenta se encuentra desactivada.'
                    return errorHandle(error)
            else:
                #Retorna un mensaje de error de 'invalid login'
                error = u'Usuario o contrasena no son correctos. Intentelo de nuevo.'
                return errorHandle(error)
        else:
            return render(request, 'appcasona/login_template.html')
    else:
        return render(request, 'appcasona/index.html')

#REMOVE WHEN LOGIN TEMPLATE IS COMPLETE
#    return render(request, 'appcasona/login_template.html')

def log_out(request):
    logout(request)
    return redirect('login')
def index(request):
    return render(request, 'appcasona/index.html')

class Inventory(PagedFilteredTableView):
    model = Inventario
    template_name = 'appcasona/inventory.html'
    filter_class = InventarioFilter
    formhelper_class=InventarioFormHelper
    table_class = InventarioTable

class Proveedores(PagedFilteredTableView):
    model = Proveedor
    template_name = 'appcasona/roveedor.html'
    filter_class = ProveedorFilter
    formhelper_class=ProveedorFormHelper
    table_class = ProveedorTable

class Platillos(PagedFilteredTableView):
    model = Platillo
    template_name = 'appcasona/platillo.html'
    filter_class = PlatilloFilter
    formhelper_class = PlatilloFormHelper
    table_class = PlatilloTable
