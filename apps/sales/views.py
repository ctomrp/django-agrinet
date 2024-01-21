from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from apps.users.views import is_userproducer, is_userclient

from django.template.loader import get_template
from django.views import View

from django.http import HttpResponse
from datetime import datetime

from django.views import View

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


@login_required
@user_passes_test(is_userproducer)
def sales_report(request):
    return render(request, "sales_report.html")


@login_required
@user_passes_test(is_userproducer)
def generate_report(request):
    return render(request, 'generate_report.html')


def sales_receipt(request):
    # Obtén los datos necesarios de la sesión
    sale_products_list = request.session.get('sale_products_list', [])
    receipt_type = request.session.get('receipt_type', '')

    # Calcula el total general
    total_general = sum(product_data['total'] for product_data in sale_products_list)

    # Obtiene la fecha actual
    current_date = datetime.now()

    # Accede al tipo de recibo directamente desde la venta
    sale = request.user.userclient.sales_set.filter(is_complete=True).latest('id')

    # Asegúrate de que la venta existe y tiene el tipo de recibo
    if sale and sale.receipt:
        receipt_type = sale.receipt

    # Agrega el total general, la fecha actual y el tipo de comprobante al contexto
    context = {
        'sale_products_list': sale_products_list,
        'total_general': total_general,
        'current_date': current_date,
        'receipt_type': receipt_type,
    }
    print(f"Full Context: {context}")
    
    return render(request, "sales_receipt.html", context)

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # Obtener la fecha actual
        current_date = datetime.now()

        # Obtener los productos de la sesión
        sale_products_list = request.session.get('sale_products_list', [])

        # Obtener el tipo de recibo de la sesión
        receipt_type = request.session.get('receipt_type', '')

        # Calcular el total general
        total_general = sum(product_data['total'] for product_data in sale_products_list)

        # Imprimir información en la consola para debuggear
        print(f"Receipt Type: {receipt_type}")
        print(f"Receipt Type Name: {receipt_type.name if receipt_type else ''}")

        # Obtener la plantilla HTML
        template_path = 'sales_receipt.html'
        template = get_template(template_path)
        
        # Agregar el total general, la fecha actual y el nombre del tipo de recibo al contexto
        context = {
            'sale_products_list': sale_products_list,
            'current_date': current_date, 
            'total_general': total_general,
            'receipt_type': receipt_type.name if receipt_type else '',  # Asegúrate de incluir el tipo de recibo en el contexto
            }

        # Imprimir información en la consola para debuggear
        print(f"Context: {context}")

        html = template.render(context)

        # Crear un objeto BytesIO para guardar el PDF
        buffer = BytesIO()

        # Crear el PDF con xhtml2pdf
        pisa.CreatePDF(html, dest=buffer)

        # Mover al principio del buffer para leer desde el principio
        buffer.seek(0)

        # Crear una respuesta HTTP con el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sales_receipt.pdf"'
        response.write(buffer.read())

        return response
