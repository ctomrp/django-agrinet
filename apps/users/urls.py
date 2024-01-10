from django.urls import path

from . import views


urlpatterns = [
    path('',views.panelControl,name='dashboard_producer'),
]
