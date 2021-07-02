from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cliente(request):
    contexto = {'form': ClientesForm }

    if request.method == 'POST':
        f = ClientesForm(request.POST)
        f.save() ## insert into .....
        contexto['mensaje'] = "guardado"
    return render(request, 'cliente.html', contexto)
