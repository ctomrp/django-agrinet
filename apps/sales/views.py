from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.users.models import UserProducer
from apps.users.views import is_userproducer, is_userclient


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
            report_starts_str = datetime.strptime(report_starts, '%Y-%m-%d').strftime('%d-%m-%Y')

        if report_ends:
            report_ends_str = datetime.strptime(report_ends, '%Y-%m-%d').strftime('%d-%m-%Y')
            
    context = {
        'report_starts_str': report_starts_str,
        'report_ends_str': report_ends_str,
        'producer': UserProducer.objects.get(pk=request.user.id),
        'current_date': datetime.now().strftime("%d-%m-%Y"),
        'sales': sales,
        'total': total
    }

    return render(request, 'sales_report.html', context)


@login_required
@user_passes_test(is_userproducer)
def generate_report(request):
    
    context = {
        'producer': UserProducer.objects.get(pk=request.user.id),
        'current_date': datetime.now().strftime("%d-%m-%Y"),
    }    
    if request.method == 'POST':
        report = {
            'report_starts': request.POST.get('report_starts'),
            'report_ends': request.POST.get('report_ends')
        }        
        return redirect(reverse('sales_report'), report)
        
    return render(request, 'generate_report.html', context)


@login_required
@user_passes_test(is_userclient)
def sales_receipt(request):
    return render(request, "sales_receipt.html")
