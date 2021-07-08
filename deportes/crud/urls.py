from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
        path('listadoCliente',  listadoCliente, name="listadoCliente"),
        path('crearCliente',  crearCliente, name="crearCliente"),
        path('modificarCliente/<id>',  modificarCliente, name="modificarCliente"),
        path('eliminarCliente/<id>',  eliminarCliente, name="eliminarCliente"),

]


# 127.0.0.1:8000/
# 127.0.0.1:8000/index