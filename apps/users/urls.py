from django.urls import path
from .views import CustomLoginView, producer_dashboard, client_dashboard
from . import views
urlpatterns = [
    path("", CustomLoginView.as_view(), name="login"),
    path("producer/", producer_dashboard, name="producer_dashboard"),
    path("client/", client_dashboard, name="client_dashboard"),
    path('producer_dashboard/',views.panelControl,name='dashboard_producer'),
    path('my_products/',views.myProducts,name='my_products'),
]
