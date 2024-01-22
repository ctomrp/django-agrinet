import locale
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


from xhtml2pdf import pisa
from io import BytesIO

from apps.users.models import UserProducer
from apps.users.views import is_userproducer, is_userclient


DATE_DMY = '%Y-%m-%d'
DATE_DMY_STR = "%d de %B de %Y"
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


@login_required
@user_passes_test(is_userproducer)
def sales_report(request):
    report_starts = None
    report_ends = None
    total = 0
    
    if request.method == 'POST':
        report_starts = request.POST.get('report_starts')
        report_ends = request.POST.get('report_ends')
        
        query = """
                SELECT 
                    pp.name,
                    pp2.name,
                    SUM(ss2.quantity),
                    SUM(ss2.quantity)*pp.price
                FROM 
                    sales_sales ss 
                    INNER JOIN
                    sales_salesproducts ss2
                    ON(ss.id = ss2.sale_id) 
                    INNER JOIN products_product pp
                    ON(pp.id = ss2.product_id)
                    INNER JOIN products_productcategory pp2 
                    ON(pp.category_id = pp2.id)
                WHERE
                    pp.producer_id = %s
                    AND
                    ss.date_sale BETWEEN %s AND %s
                GROUP BY
                    pp.name, pp2.name
                ORDER BY
                    3 DESC
                ;
                """
                
        with connection.cursor() as cursor:
            cursor.execute(query, [request.user.id, report_starts, report_ends])
            sales = cursor.fetchall()
            total = sum([total + sale[3] for sale in sales])
       
        if report_starts:
            report_starts_str = datetime.strptime(report_starts, DATE_DMY).strftime(DATE_DMY_STR)

        if report_ends:
            report_ends_str = datetime.strptime(report_ends, DATE_DMY).strftime(DATE_DMY_STR)
            
    context = {
        'report_starts_str': report_starts_str,
        'report_ends_str': report_ends_str,
        'producer': UserProducer.objects.get(pk=request.user.id),
        'current_date': datetime.now().strftime(DATE_DMY_STR),
        'sales': sales,
        'total': total
    }

    return render(request, 'sales_report.html', context)


@login_required
@user_passes_test(is_userproducer)
def generate_report(request):     
    if request.method == 'POST':       
        return redirect(reverse('sales_report'))
    
    context = {
        'producer': UserProducer.objects.get(pk=request.user.id),
        'current_date': datetime.now().strftime(DATE_DMY_STR),
    }  
    return render(request, 'generate_report.html', context)


@login_required
@user_passes_test(is_userclient)
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
        print(f"Receipt Type Name: {receipt_type if receipt_type else ''}")

        # Obtener la plantilla HTML
        template_path = 'sales_receipt.html'
        template = get_template(template_path)
        
        # Agregar el total general, la fecha actual y el nombre del tipo de recibo al contexto
        context = {
            'sale_products_list': sale_products_list,
            'current_date': current_date, 
            'total_general': total_general,
            'receipt_type': receipt_type if receipt_type else '',  # Asegúrate de incluir el tipo de recibo en el contexto
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
        response['Content-Disposition'] = f'attachment; filename="sales_receipt_{current_date}.pdf"'
        response.write(buffer.read())

        return response