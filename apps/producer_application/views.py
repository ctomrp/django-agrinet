from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404


from .forms import ApplicationFormForm
from .models import ApplicationForm, ApplicationFormState

def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationFormForm(request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.state = ApplicationFormState.objects.get(id=10)
            new_application.save()
            return redirect('login')

    return render(request, 'producer_application.html', {
        'form': ApplicationFormForm
    })
    
   
        
@login_required  
def list_applications(request):
    applications = ApplicationForm.objects.all()
    return render(request, "application_status.html", {'applications': applications})


@login_required
def application_detail(request, application_id):
    application = get_object_or_404(ApplicationForm, pk=application_id)   
    return render(request, 'application_detail.html', {'application': application})