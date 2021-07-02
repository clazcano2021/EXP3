from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('cliente', cliente, name='cliente'),

]


# 127.0.0.1:8000/
# 127.0.0.1:8000/index