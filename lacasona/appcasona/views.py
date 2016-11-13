#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import Inventario, Platillo, Orden

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



def log_out(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, "appcasona/index.html")


def search_form(request):
    return render(request, 'appcasona/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        inventario = Inventario.objects.filter(nombreDelProducto__icontains=q)
        return render(request, 'appcasona/search.html',
                      {'Inventario': inventario, 'query': q})
    else:
        return render(request, 'appcasona/search_form.html', {'error': True})



# Vista del menu
def menu(request):
    platillos = Platillo.objects.all()
    image_sources = Platillo.objects.filter()
    return render(request, "appcasona/menu.html", {'platillos':platillos})


def platillo_detail(request, platillo_id):
    context = RequestContext(request)
    plato = get_object_or_404(Platillo, pk=platillo_id)
    ingredientes = plato.ingredientes.all()

    context_dict = {'nombre': plato.nombreDelPlatillo,
                    'descripcion': plato.descripcionPlatillo,
                    'precio': str(plato.precioPlatillo),
                    'imagen': plato.imagenPlatillo,
                    'ingredientes': ingredientes}

    return render_to_response("appcasona/descripcion.html",context_dict, context)
