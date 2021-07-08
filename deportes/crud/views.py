from .forms import *
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoCliente(request):
#ORM django
    listado = Clientes.objects.all() # select * from cliente
    contexto = {'listado' : listado, 'user': 'alguien' }
    return render(request, 'listadoCliente.html', contexto)


def crearCliente(request):
    contexto = {'form' : ClientesForm }

    if request.method == 'POST':
        cliente = ClientesForm(request.POST)
        cliente.save() # insert...
        contexto['mensaje'] = 'Datos guardados'

    return render(request, 'crearCliente.html', contexto)


def modificarCliente(request, id):
    cliente = Clientes.objects.get(id = id)
    contexto = {'form' : ClientesForm(instance=cliente) }


# permite capturar los valores del form y guardarlos en la BDD
    if request.method == 'POST': # detecta si hay una solicitud (presionó el botón)
        formulario = ClientesForm(data=request.POST, instance=cliente)
        formulario.save()
        contexto = {'form' : ClientesForm(instance=Clientes.objects.get(id = id)) }
        contexto['mensaje'] = 'Los datos fueron guardado'
    
    return render(request, 'modificarCliente.html', contexto)


# agregar redirect al import : from django.shortcuts import render, redirect
def eliminarCliente(request, id):
    cliente = Clientes.objects.get(id = id) # where idCliente = id
    cliente.delete()
    return redirect(to = "listadoCliente") 

