import itertools
from .models import Inventario, Platillo, Orden, Cantidad

def resta(lista, nombre):
	#donde dice "carne", se debe poner el nombre del platillo que rafa manda.
	ingredientes = Platillo.objects.get(nombreDelPlatillo = nombre).ingredientes.all()
	

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
	
	
	z=len(ingredientes)-1
	while z>=0:
		nombreIngrediente= ingredientes[z]    #nombre del ingrediente a buscar
		idInventario= Inventario.objects.get(nombreDelProducto=nombreIngrediente).id #id del ingrediente en la base de datos 
		idPlatillo= Platillo.objects.get(nombreDelPlatillo=nombre).id #id del platillo en la base de datos
		porcion = Cantidad.objects.get(inventario_id = idInventario, platillo_id = idPlatillo) #cantidad de ese ingrediente en el platillo
		porcionARestar= porcion.cantidad
		cantidadInventario = Inventario.objects.get(nombreDelProducto=nombreIngrediente).cantidadDeProducto #cantidad de ese producto que hay en inventario
		nuevaCantidad = int(cantidadInventario) - int(porcionARestar) #va a ser la nueva cantidad del Producto en inventario
		Inventario.objects.filter(nombreDelProducto=nombreIngrediente).update(cantidadDeProducto=nuevaCantidad) #Actualiza la cantidad del producto en inventario 
		z=z-1
		



		
		
#porcion = Cantidad.objects.get(inventario_id=idInventario,platillo_id=idPlatillo)
#porcion.cantidad

		
#Actualizar la cantidad que hay en la base de datos
#Inventario.objects.filter(nombreDelProducto=nombreIngrediente).update(cantidadDeProducto=resta) 

#Me da la cantidad que hay en la base de datos 
#Inventario.objects.get(nombreDelProducto=nombreIngrediente).cantidadDeProducto

#La id del ingrediente 
#idInventario= Inventario.objects.get(nombreDelProducto=nombreIngrediente).id

#La id del platillo
#idPlatillo= Platillo.objects.get(nombreDelPlatillo=nombre).id


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
