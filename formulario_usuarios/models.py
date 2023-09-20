from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_telefonico = models.CharField(max_length=15)  # Ajusta la longitud según tus necesidades
