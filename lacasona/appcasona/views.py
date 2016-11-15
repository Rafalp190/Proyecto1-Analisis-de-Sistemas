#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import Inventario, Platillo, Orden
from django.views.decorators.csrf import csrf_protect
import datetime
from django.http import Http404
from restaInventario import resta

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
@csrf_protect
def menu(request):
    platillos = Platillo.objects.all()
    image_sources = Platillo.objects.filter()
    return render(request, "appcasona/menu.html", {'platillos':platillos})


def cocina(request):
    if request.GET.get('completed'):
        order_id = request.GET['completed']
        one_entry = Orden.objects.get(pk=order_id)
        one_entry.status = 1
        one_entry.save()

        ordenes = Orden.objects.all()
        return render(request, "appcasona/cocina.html", {'ordenes': ordenes})
    else:
        ordenes = Orden.objects.all()
        return render(request, "appcasona/cocina.html", {'ordenes': ordenes})


#View de la caja
def caja (request):
    if request.GET.get('cancel'):
        order_id = request.GET['cancel']
        one_entry = Orden.objects.get(pk=order_id)
        one_entry.status = 2
        one_entry.save()

        ordenes = Orden.objects.all()
        return render(request, "appcasona/caja.html", {'ordenes': ordenes})
    else:
        ordenes = Orden.objects.all()
        return render(request, "appcasona/caja.html", {'ordenes': ordenes})


@csrf_protect
def platillo_detail(request, platillo_id):
    context = RequestContext(request)
    plato = get_object_or_404(Platillo, pk=platillo_id)
    ingredientes = plato.ingredientes.all()

    context_dict = {'id': plato.platillo_id(),
                    'nombre': plato.nombreDelPlatillo,
                    'descripcion': plato.descripcionPlatillo,
                    'precio': str(plato.precioPlatillo),
                    'imagen': plato.imagenPlatillo,
                    'ingredientes': ingredientes}

    return render_to_response("appcasona/descripcion.html",context_dict, context)



def ordenar(request, platillo_id):
    #AQUI VA EL IMPORT DE RESTA INVENTARIO
    if request.method == "POST":
        if "volver" in request.POST:
            return redirect('menu')
        choices = request.POST.getlist("opciones")
        plato = get_object_or_404(Platillo, pk=platillo_id)
        mesa = request.POST["mesa"]
        #Se obtiene el usuario actual
        if request.user.is_authenticated():
            username = request.user.username
        #Se obtiene la fecha y hora actual
        datime = datetime.datetime.now()
        #Se busca una orden con los parametros establecidos
        try:
            order = Orden.objects.get(mesa=mesa, nombreDelMesero=username, status=0)
        except Orden.DoesNotExist:
            order = None
        #Se crea la orden si no existe
        if order == None:
            order = Orden(nombreDelMesero=username,mesa=mesa,fecha=datime,status=0)
            order.save()
        order.platillos.add(plato)

        ing=[]
        nombrePlato=plato.nombreDelPlatillo
        for i in choices:
            invN= Inventario.objects.get(id=i)
            ing.append(str(invN.nombreDelProducto))

        # AQUI VA LO DE RESTA INVENTARIO
        # NOMBRE DE LA LISTA = ing
        # NOMBRE DEL PLATILLO = nombrePlato

	resta(ing,nombrePlato)

        if "botonOtro" in request.POST:
            return redirect('menu')

        elif "complete" in request.POST:
            return redirect('caja')
    return redirect('menu')

def carrito (request):
    inventario = Inventario.objects.all()
    return render(request, "appcasona/carrito.html", {'inventario': inventario})

def pagos(request):
    if request.GET.get('cancel'):
        order_id = request.GET['cancel']
        orden = Orden.objects.get(pk=order_id)
        return render(request, "appcasona/pagos.html", {'orden': orden,})

    elif request.GET.get('bill'):
        order_id = request.GET['bill']
        orden = Orden.objects.get(pk=order_id)
        orden.status = 2
        orden.save()

        ordenes = Orden.objects.all()
        return redirect('caja')

    else:
        return HttpResponse(status=404)