import itertools
from .models import Inventario, Platillo, Orden, Cantidad

def resta(lista, nombre)
	#donde dice "carne", se debe poner el nombre del platillo que rafa manda.
	ingredientes = Platillo.objects.get(nombreDelPlatillo = nombre).ingredientes.all()
	print ingredientes


	x=len(ingredientes)-1
	y=len(lista)-1
	while x>=0:
	        while y>=0:
	                if ingredientes[x]==lista[y]:
	                        ingredientes.pop(x)
	                else:
	                        break
	                y=y-1
	        y=len(lista)-1
	        x=x-1
	print ingredientes





#a mi me pasan el nombre del platillo, y ingredientes que no quiere del mismo
#busco el nombre del platillo y guardo sus ingredientes en una lista
#comparo la lista con la bin list que me manda
#quito de la lista los que estan en la otra
#de cada ingrediente busco la cantidad que lleva ese platillo
#guardo eso en variables y las resto del inventario

#Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
#enPlatillo = tuple(x for x in ingredientes if x not in set(list))
#[x for x in l1 if x not in l2]





#resta																				   pablo y andres
#views - cocina, orden , descripcion de platillo, caja                                 rafa y moi
# templates - cocina, orden , descripcion de platillo, caja							   rafa y moi
#prueba color 											                               pablo
