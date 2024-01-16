from django.urls import path
from . import  views


urlpatterns = [
    path('application_form/', views.application_form_view, name='application_form'),
    path('edit-application-form/<int:form_id>/', views.edit_application_form, name='edit_application_form'),
    path('delete-application-form/<int:form_id>/', views.delete_application_form, name='delete_application_form')
   

]


