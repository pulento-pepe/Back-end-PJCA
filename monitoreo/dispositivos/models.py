"""class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre"""
# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Zona(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.CASCADE,
        related_name="dispositivos",
        null=True,   # 🔹 permite NULL en BD
        blank=True   # 🔹 permite dejar vacío en formularios/admin
    )
    zona = models.ForeignKey(
        "Zona",
        on_delete=models.CASCADE,
        related_name="dispositivos",
        null=True,
        blank=True
    )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Medicion(models.Model):
    dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        related_name="mediciones"
    )
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.dispositivo.nombre} - {self.consumo} kWh ({self.fecha_hora})"


class Alerta(models.Model):
    dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        related_name="alertas"
    )
    medicion = models.ForeignKey(
        Medicion,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name="alertas"
    )
    descripcion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alerta en {self.dispositivo.nombre} - {self.descripcion}"

