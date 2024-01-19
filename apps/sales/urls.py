from django.urls import path

from . import views
from .views import GeneratePdf


urlpatterns = [
    path("sales_report/", views.sales_report, name="sales_report"),
    path("sales_receipt/", views.sales_receipt, name="sales_receipt"),
    path("generate_report/", views.generate_report, name="generate_report"),
    path('generar_pdf/', GeneratePdf.as_view(), name='generate_pdf'),
]