"""
URL configuration for diablo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from diabloapp import views
from django.contrib import admin
from django.urls import path
from formulario_usuarios import views1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('otro/', views.puto, name='home'),
    path('', views.mi_vista, name='mi_vista'),
    path('gitk/', views.nuevo, name='nuevo'),
    path('none/', views.trato, name='nuevo'),
    path('user/', views.user, name='user'),
    path('agregar_usuario/', views1.agregar_usuario, name='agregar_usuario'),
]
