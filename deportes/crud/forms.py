from django import forms
from .models import *

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields= '__all__'

class PlanesForm(forms.ModelForm):

    class Meta:
        model = Planes
        fields= '__all__'

class DeporteForm(forms.ModelForm):

    class Meta:
        model = Deporte
        fields= '__all__'