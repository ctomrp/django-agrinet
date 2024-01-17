from django.db import models

from apps.products.models import Product
from apps.users.models import UserClient

# Create your models here.
class ShippingMethod(models.Model):
    shipping_method_name = models.CharField(max_length=60, verbose_name="Shipping Method Name")

    def __str__(self):
        return self.shipping_method_name

class PaymentMethod(models.Model):
    payment_method_name = models.CharField(max_length=30, verbose_name="Payment Method Name")

    def __str__(self):
        return self.payment_method_name

class ReceiptType(models.Model):
    receipt_type_name = models.CharField(max_length=30, verbose_name="Receipt Type Name")

    def __str__(self):
        return self.receipt_type_name
    


class Sales(models.Model):
    client = models.ForeignKey(UserClient, on_delete=models.CASCADE, verbose_name="Client")
    date_sale = models.DateField(auto_now_add=True, verbose_name="Date Sale")
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, blank=True,null=True, verbose_name="Payment")
    shipping = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE, blank=True,null=True,verbose_name="Shipping")
    receipt = models.ForeignKey(ReceiptType, on_delete=models.CASCADE, blank=True,null=True,verbose_name="Receipt")
    is_complete = models.BooleanField(default=False)
    total = models.IntegerField(blank=True,null=True, verbose_name="total")
    
    def __str__(self):
        return str(self.id)


    
class SalesProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE,verbose_name="Sale")
    quantity = models.IntegerField(default=0, verbose_name="Units")
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


    def __str__(self):
        return f"{self.sale.id} - Product: {self.product.name} - Quantity: {self.quantity}"