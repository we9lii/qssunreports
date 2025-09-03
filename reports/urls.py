from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    # إنشاء التقارير
    path('sales/create/', views.create_sales_report, name='create_sales'),
    path('field/create/', views.create_field_report, name='create_field'),
    path('customer/create/', views.create_customer_report, name='create_customer'),
    path('create/', views.create_report_choice, name='create_report'),

    # عرض التقارير السابقة
    path('my/', views.my_reports, name='my_reports'),

    # تصدير التقارير كـ PDF
    path('export/sales/pdf/', views.sales_report_pdf, name='sales_pdf'),
]