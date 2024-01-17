from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AplicationFormState(models.Model):
    state_name = models.CharField(max_length=40)

    def __str__(self):
        return self.state_name

class ApplicationForm(models.Model):
    dni = models.CharField(max_length=12, )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    phone_number = models.CharField(max_length=20)
    bussiness_name = models.CharField(max_length=255)
    birth_date = models.DateField(verbose_name=("Fecha de nacimiento"))
    state = models.ForeignKey(AplicationFormState, on_delete=models.CASCADE, verbose_name=("Status"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.state}"