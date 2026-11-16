from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    radio_metros = models.IntegerField()

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)
    dentro_de_zona = models.BooleanField(default=False)
    consentimiento_fecha = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Conserje(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha_hora = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.fecha_hora}"


class Aviso(models.Model):
    ESTADOS = [
        ("PE", "Pendiente"),
        ("AT", "Atendido"),
        ("CA", "Cancelado"),
    ]

    distancia_metros = models.FloatField()
    estado = models.CharField(max_length=2, choices=ESTADOS, default="PE")
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conserje = models.ForeignKey(Conserje, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Aviso {self.id} - {self.estado}"