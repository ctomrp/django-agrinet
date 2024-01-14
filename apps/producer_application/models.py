from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class applicationForm(models.Model):
    dni = models.CharField(max_length=12, )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    phonenumber = models.CharField(max_length=20)
    bussinessname = models.CharField(max_length=255)
    producertype = models.CharField(max_length=300)
    birthdate = models.DateField(verbose_name=("Fecha de nacimiento"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"