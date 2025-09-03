from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

# نماذج التقارير
from .models import SalesReport, FieldReport, CustomerReport, Notification

# نماذج النماذج (Forms)
from .forms import SalesReportForm, FieldReportForm, CustomerReportForm


# 1. إنشاء تقرير المبيعات
@login_required
def create_sales_report(request):
    if request.method == 'POST':
        form = SalesReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.employee = request.user.employee
            report.save()
            return redirect(reverse('staff:dashboard'))
    else:
        form = SalesReportForm()
    return render(request, 'reports/sales_form.html', {'form': form})


# 2. إنشاء تقرير الفنيين الميدانيين
@login_required
def create_field_report(request):
    if request.method == 'POST':
        form = FieldReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.employee = request.user.employee
            report.save()
            return redirect(reverse('staff:dashboard'))
    else:
        form = FieldReportForm()
    return render(request, 'reports/field_form.html', {'form': form})


# 3. إنشاء تقرير ملاحظات العملاء
@login_required
def create_customer_report(request):
    if request.method == 'POST':
        form = CustomerReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.employee = request.user.employee
            report.save()
            return redirect(reverse('staff:dashboard'))
    else:
        form = CustomerReportForm()
    return render(request, 'reports/customer_form.html', {'form': form})


# 4. عرض التقارير السابقة للموظف
@login_required
def my_reports(request):
    try:
        employee = request.user.employee
    except:
        employee = None
        return render(request, 'reports/my_reports.html', {'employee': None})

    sales_reports = SalesReport.objects.filter(employee=employee).order_by('-date')
    field_reports = FieldReport.objects.filter(employee=employee).order_by('-date')
    customer_reports = CustomerReport.objects.filter(employee=employee).order_by('-date')

    return render(request, 'reports/my_reports.html', {
        'employee': employee,
        'sales_reports': sales_reports,
        'field_reports': field_reports,
        'customer_reports': customer_reports,
    })


# 5. تصدير تقارير المبيعات كـ PDF
@login_required
def sales_report_pdf(request):
    try:
        employee = request.user.employee
        reports = SalesReport.objects.filter(employee=employee).order_by('-date')
    except:
        return HttpResponse("خطأ: لا يمكن تحميل التقرير")

    # تحميل القالب
    html_string = render_to_string('reports/pdf_template.html', {
        'employee': employee,
        'reports': reports,
        'title': 'تقرير المبيعات'
    })

    # إنشاء استجابة PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="تقرير_المبيعات.pdf"'

    # تحويل HTML إلى PDF
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
        return HttpResponse('حدث خطأ أثناء إنشاء PDF')

    return response
@login_required
def create_report_choice(request):
    return render(request, 'reports/create_choice.html')