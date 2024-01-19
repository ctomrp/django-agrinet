from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from apps.users.views import is_userproducer, is_userclient

from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa  # Instala esta librería con pip install xhtml2pdf
import os
from django.http import HttpResponse



@login_required
@user_passes_test(is_userproducer)
def sales_report(request):
    return render(request, "sales_report.html")


@login_required
@user_passes_test(is_userproducer)
def generate_report(request):
    return render(request, 'generate_report.html')


def sales_receipt(request):
    sale_products_list = request.session.get('sale_products_list', [])

    # Calcula el total general
    total_general = sum(product_data['total'] for product_data in sale_products_list)

    # Agrega el total general al contexto
    context = {'sale_products_list': sale_products_list, 'total_general': total_general}

    print(sale_products_list)
    return render(request, "sales_receipt.html", context)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        sale_products_list = request.session.get('sale_products_list', [])

        context = {
            'sale_products_list': sale_products_list,
        }

        template_path = 'sales_receipt.html'
        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sales_receipt.pdf"'

        pisa.CreatePDF(html, dest=response)

        return response