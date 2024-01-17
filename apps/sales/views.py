from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.users.views import is_userproducer, is_userclient

# Create your views here.
@login_required
@user_passes_test(is_userproducer)
def sales_report(request):
    return render(request, "sales_report.html")


@login_required
@user_passes_test(is_userproducer)
def generate_report(request):
    return render(request, 'generate_report.html')


@login_required
@user_passes_test(is_userclient)
def sales_receipt(request):
    return render(request, "sales_receipt.html")
