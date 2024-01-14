from django.db import models

# Create your models here.

class formulario(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=255)
    tipo_productor = models.CharField(max_length=100)
    fecha_nac = models.DateField(verbose_name=("Fecha de nacimiento"))

    def __str__(self):
        return f"{self.nombre} {self.apellido}"