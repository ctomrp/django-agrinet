from django.shortcuts import render, redirect
from django.http import HttpRequest

from .forms import ApplicationFormForm
from .models import ApplicationForm, AplicationFormState


def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationFormForm(request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.state = AplicationFormState.objects.get(id=10)
            new_application.save()
            return redirect('login')

    return render(request, 'producer_application.html', {
        'form': ApplicationFormForm
    })
        