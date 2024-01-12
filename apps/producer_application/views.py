
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ApplicationForm



def application_form_view(request):

    if request.method == 'GET':
            return render(request, 'producer_application.html',{
                'form': ApplicationForm
            }) 
    else:
        try:
            form = ApplicationForm(request.POST)
            new_application = form.save(commit=False)
            new_application.save()
            return redirect('/')
        except Exception as e:
             return render(request, 'producer_application.html',{
                'form': ApplicationForm,
                'error': e

                })
    
