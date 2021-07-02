from django.urls import path
from .views import *
urlpatterns = [

    path('listaCategoria',listaCategoria, name='listaCategoria'),

]