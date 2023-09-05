from django.shortcuts import render
from django.http import HttpResponse
import datetime

def puto(request):
    return HttpResponse("esta es la app tarde un poco pero ya quedo")
def mi_vista(request):
    mensaje = "este es el mensaje cambiado referenciado a la html"
    dt = datetime.datetime.now()
    return render(request, 'diablo_app/plantilla.html', {'mensaje': mensaje, 'fecha': dt})