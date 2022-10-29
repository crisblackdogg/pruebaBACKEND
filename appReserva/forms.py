from unittest.util import _MAX_LENGTH
from django import forms
from appReserva.models import reserva
from.models import reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = reserva
        fields = '__all__'

class reservaForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    telefono = forms.IntegerField(min_value=6, max_value=8)
    fecha = forms.DateField()
    hora = forms.TimeField()
    cantidadPersonas = forms.IntegerField(min_value=1, max_value=15) 
    