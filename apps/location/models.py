from django.db import models
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    name = models.CharField(max_length=45,verbose_name=_("Region"))

    def str(self):
        return self.name


class Commune(models.Model):
    name = models.CharField(max_length=45, verbose_name=_("Commune"))
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def str(self):
        return self.name
