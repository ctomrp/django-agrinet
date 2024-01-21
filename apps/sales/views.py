from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
import locale

from apps.users.models import UserProducer
from apps.users.views import is_userproducer, is_userclient

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
            report_starts_str = datetime.strptime(report_starts, '%Y-%m-%d').strftime("%d de %B de %Y")

        if report_ends:
            report_ends_str = datetime.strptime(report_ends, '%Y-%m-%d').strftime("%d de %B de %Y")
            
    context = {
        'report_starts_str': report_starts_str,
        'report_ends_str': report_ends_str,
        'producer': UserProducer.objects.get(pk=request.user.id),
        'current_date': datetime.now().strftime("%d de %B de %Y"),
        'sales': sales,
        'total': total
    }

    return render(request, 'sales_report.html', context)


@login_required
@user_passes_test(is_userproducer)
def generate_report(request):
    return render(request, 'generate_report.html')


@login_required
@user_passes_test(is_userclient)
def sales_receipt(request):
    sale_products_list = request.session.get('sale_products_list', [])

    total_general = sum(product_data['total'] for product_data in sale_products_list)
    
    context = {'sale_products_list': sale_products_list, 'total_general': total_general}

    print(sale_products_list, total_general,)
    return render(request, "sales_receipt.html", context)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        try:
            sale_products_list = request.session.get('sale_products_list', [])
            context = {'sale_products_list': sale_products_list}
            template_path = 'sales_receipt.html'
            template = get_template(template_path)
            html = template.render(context)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="sales_receipt.pdf"'

            pisa.CreatePDF(html, dest=response)
            return response
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la generación del PDF
            print(f"Error generando PDF: {e}")
            return HttpResponseServerError("Error generando el PDF")