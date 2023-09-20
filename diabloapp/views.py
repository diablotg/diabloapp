from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse


def puto(request):
    return HttpResponse("esta es la app tarde un poco pero ya quedo")
def mi_vista(request):
    mensaje = "Prueba de Django en Python"
    dt = datetime.now()
    return render(request, 'diablo_app/plantilla.html', {'mensaje': mensaje, 'fecha': dt})

def nuevo(request):
    return HttpResponse("modificacion de gitk")

def nada():
    return None

def trato(request):
    resultado = nada()==None
    return HttpResponse(resultado)

def user(request):
    user_data = {
        'nombre': 'Jesus Eduardo Torres Garfias',
        'email': 'diablo@gmail.com',
        'edad': 28,
    }
    return JsonResponse(user_data)
