from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'branch', 'phone')
    list_filter = ('department', 'branch')
    search_fields = ('user__first_name', 'user__last_name', 'phone', 'branch')