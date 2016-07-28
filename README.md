# Proyecto1-Analisis-de-Sistemas

#Prerequerimientos:
-instalar mySQL Workbench 6.3
	-Crear Base de datos:
		Instrucciones:
		En la consola
		
		 $sudo mysql -u root -p
		 password: ""
		 create database lacasona;
		 
-instalar python 2.7
	-Configurar variables de entorno de Python y Python/scripts
	-Instalar PIP
	En la Consola
	
		$python get-pip.py
		
-Descargar mySQL para python en el siguiente sitio:
	
	https://pypi.python.org/pypi/MySQL-python 	

Instalaciones en PIP
-
-Instalar django

	$pip install Django==1.9
-Instalar las funcionalidades de django adicionales

	$ pip install django_nvd3 
	$ pip install django_tables2
	$ pip install django_ﬁlters 
	$ pip install --upgrade django-crispy-forms 

Inicializar el Servidor
-
Descargar el Repositorio

1. Abrir una consola
2. Cambiar el directorio a donde se encuentra el repositorio 

	*\Proyecto1-Analisis-de-Sistemas\lacasona

3. Escribir los siguientes comandos:

	$ python manage.py migrate
	$ python manage.py createsuperuser
	$ python manage.py runserver
	
-nota para correr el servidor de nuevo solamente es necesario

	$ python manage.py runserver
4. Dirigirse a su buscador preferido de internet
	Dirigirse a su URL local:
	
	http://127.0.0.1:8000/

5. Inicie sesion con la información de su usuario

	