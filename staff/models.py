from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DEPARTMENTS = [
        ('sales', 'قسم المبيعات'),
        ('field_tech', 'فنيون ميدانيون'),
        ('customer_service', 'ملاحظات العملاء'),
    ]
    department = models.CharField(max_length=20, choices=DEPARTMENTS)
    phone = models.CharField(max_length=15, blank=True)
    branch = models.CharField(max_length=100, verbose_name="الفرع")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.get_department_display()}"