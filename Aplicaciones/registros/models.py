from django.db import models

# Create your models here.
from django.db import models

class Ciudad(models.Model):
    nombre_city = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_city

class Propietario(models.Model):
    nombre_prop = models.CharField(max_length=200)
    apellido_prop = models.CharField(max_length=200)
    email_prop = models.EmailField(max_length=200)
    telefono_prop = models.CharField(max_length=12)
    fk_id_city = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre_prop} {self.apellido_prop}'

class Modelo(models.Model):
    nombre_mod = models.CharField(max_length=200)
    estado_mod = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_mod

class Vehiculo(models.Model):
    fk_id_mod = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    fabricacion_veh = models.IntegerField()
    precio_veh = models.DecimalField(max_digits=10, decimal_places=2)
    color_veh = models.CharField(max_length=50)
    placa_veh = models.CharField(max_length=10)

    def __str__(self):
        return self.placa_veh
