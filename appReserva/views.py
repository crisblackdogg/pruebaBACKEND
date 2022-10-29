from django.shortcuts import get_object_or_404, redirect, render
from appReserva.models import reserva
from appReserva.forms import FormReserva
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoReserva(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
    formulario = reserva.objects.get(id = id)
    formulario.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    formulario = reserva.objects.get(id = id)
    form = FormReserva(instance=formulario)
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=formulario)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarReserva.html', data)
    





    