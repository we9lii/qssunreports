from django.db import models
from staff.models import Employee

# 1. تقرير المبيعات
class SalesReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    clients_visited = models.PositiveIntegerField(verbose_name="عدد العملاء الذين تم زياراتهم")
    proposals_sent = models.PositiveIntegerField(verbose_name="عدد العروض المقدمة")
    deals_closed = models.PositiveIntegerField(verbose_name="عدد الصفقات المغلقة")
    total_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قيمة العروض (ريال)")
    interested_clients = models.TextField(verbose_name="العملاء المهتمين", blank=True)
    next_appointments = models.TextField(verbose_name="المواعيد القادمة", blank=True)

    def __str__(self):
        return f"مبيعات - {self.employee} - {self.date}"

# 2. تقرير الفنيين الميدانيين
class FieldReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    sites_count = models.PositiveIntegerField(verbose_name="عدد المواقع")
    MAINTENANCE_TYPES = [
        ('inspection', 'فحص'),
        ('installation', 'تركيب'),
        ('repair', 'إصلاح'),
    ]
    maintenance_type = models.CharField(max_length=15, choices=MAINTENANCE_TYPES, verbose_name="نوع الصيانة")
    condition_after = models.CharField(max_length=50, verbose_name="حالة النظام بعد الصيانة")
    materials_used = models.TextField(verbose_name="المواد المستهلكة", blank=True)
    location = models.CharField(max_length=100, blank=True, verbose_name="الموقع (GPS)")
    photo_before = models.ImageField(upload_to='field/before/', blank=True, null=True, verbose_name="صورة قبل")
    photo_after = models.ImageField(upload_to='field/after/', blank=True, null=True, verbose_name="صورة بعد")

    def __str__(self):
        return f"ميداني - {self.employee} - {self.date}"

# 3. تقرير ملاحظات العملاء
class CustomerReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميل")
    phone = models.CharField(max_length=15, verbose_name="رقم التواصل")
    ISSUE_TYPES = [
        ('complaint', 'شكوى'),
        ('suggestion', 'اقتراح'),
        ('appreciation', 'شكر'),
    ]
    issue_type = models.CharField(max_length=15, choices=ISSUE_TYPES, verbose_name="نوع الملاحظة")
    details = models.TextField(verbose_name="تفاصيل الملاحظة")
    PRIORITY = [
        ('urgent', 'عاجل'),
        ('normal', 'عادي'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY, verbose_name="الأولوية")
    follow_up_date = models.DateField(verbose_name="موعد المتابعة")
    STATUS = [
        ('open', 'مفتوح'),
        ('closed', 'مغلق'),
    ]
    status = models.CharField(max_length=10, choices=STATUS, default='open', verbose_name="الحالة")

    def __str__(self):
        return f"عميل - {self.customer_name} - {self.issue_type}"
class Notification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name="العنوان")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title