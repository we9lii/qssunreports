from django import forms
from .models import SalesReport, FieldReport, CustomerReport

class SalesReportForm(forms.ModelForm):
    class Meta:
        model = SalesReport
        fields = '__all__'
        exclude = ['employee', 'date']
        labels = {
            'clients_visited': 'عدد العملاء الذين تم زياراتهم',
            'proposals_sent': 'عدد العروض المقدمة',
            'deals_closed': 'عدد الصفقات المغلقة',
            'total_value': 'قيمة العروض (ريال)',
            'interested_clients': 'العملاء المهتمين',
            'next_appointments': 'المواعيد القادمة',
        }

class FieldReportForm(forms.ModelForm):
    class Meta:
        model = FieldReport
        fields = '__all__'
        exclude = ['employee', 'date']
        labels = {
            'sites_count': 'عدد المواقع',
            'maintenance_type': 'نوع الصيانة',
            'condition_after': 'حالة النظام بعد الصيانة',
            'materials_used': 'المواد المستهلكة',
            'location': 'الموقع (GPS)',
            'photo_before': 'صورة قبل',
            'photo_after': 'صورة بعد',
        }

class CustomerReportForm(forms.ModelForm):
    class Meta:
        model = CustomerReport
        fields = '__all__'
        exclude = ['employee', 'date']
        labels = {
            'customer_name': 'اسم العميل',
            'phone': 'رقم التواصل',
            'issue_type': 'نوع الملاحظة',
            'details': 'تفاصيل الملاحظة',
            'priority': 'الأولوية',
            'follow_up_date': 'موعد المتابعة',
            'status': 'الحالة',
        }