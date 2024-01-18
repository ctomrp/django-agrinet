from django.urls import path
from . import  views


urlpatterns = [
    path('application_form/', views.create_application_form, name='application_form'),
    path('application_status/', views.list_applications, name='application_status'),
    path('application_detail/<int:application_id>/', views.application_detail, name='application_detail'),
    path('update_application_form/<int:application_id>/', views.update_application_form, name='update_application_form'),
]
