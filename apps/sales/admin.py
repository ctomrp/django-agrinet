from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sales)
admin.site.register(SalesProducts)
admin.site.register(PaymentMethod)
admin.site.register(ShippingMethod)
admin.site.register(ReceiptType)