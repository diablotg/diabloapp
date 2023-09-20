from django.shortcuts import render, redirect
from .forms import UsuarioForm

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_usuario')  # Redirige a una página exitosa o donde desees
    else:
        form = UsuarioForm()
    
    return render(request, 'agregar_usuario.html', {'form': form})