from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import UserProducer


class ProductCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name=_("Category name"))

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name=_("Product name"))
    price = models.IntegerField(verbose_name=_("Price"))
    stock = models.IntegerField(verbose_name=_("Products in stock"))
    description = models.TextField(verbose_name=_("Description"))
    picture = models.ImageField(upload_to="", verbose_name=_("Picture"))
    category = models.ForeignKey(
        "ProductCategory",
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
    )
    producer = models.ForeignKey(
        UserProducer, on_delete=models.CASCADE, verbose_name=_("Producer")
    )

    def __str__(self):
        return self.name
