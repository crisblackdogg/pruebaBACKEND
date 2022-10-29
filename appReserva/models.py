
from django import forms
from django.db import models
from django.forms import IntegerField


# Create your models here.

estado = [
 [0, "RESERVADO"],
 [1,"COMPLETADA"],
 [2,"ANULADA"],
 [3,"NO ASISTEN"]
]

cantidadPersonas = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (14,14),
    (15,15)
]

class reserva(models.Model):
    nombre = models.CharField(max_length=70)
    telefono = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    cantidadPersonas = models.IntegerField(choices= cantidadPersonas) 
    estadoReserva = models.IntegerField(choices= estado)
    observaccion = models.TextField()

