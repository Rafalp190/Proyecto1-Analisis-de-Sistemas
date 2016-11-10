


def restainventario(str,list):
	
	ingredientes= platillo.objetcs.filter(str)   			    #es una lista de los ingredientes del platillo
	enPlatillo = [x for x in ingredientes if x not in list]  	#quito los ingredientes que estan en list de ingredientes
	x=0				
	#inicio mi contador
	for i in enPlatillo:									
	inventario.objetcs.filter(nombreDelProducto=enPlatillo[x]	).update(cantidadDeProducto=resta)
	ingre
	x=x+1
	







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



