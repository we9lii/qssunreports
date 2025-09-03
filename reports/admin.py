from django.contrib import admin
from .models import SalesReport, FieldReport, CustomerReport, Notification

@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'clients_visited', 'deals_closed')
    list_filter = ('date', 'employee')
    search_fields = ('employee__user__first_name', 'interested_clients')

@admin.register(FieldReport)
class FieldReportAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'sites_count', 'maintenance_type')
    list_filter = ('maintenance_type', 'date')
    search_fields = ('employee__user__first_name', 'location')

@admin.register(CustomerReport)
class CustomerReportAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'issue_type', 'priority', 'status', 'follow_up_date')
    list_filter = ('issue_type', 'priority', 'status', 'follow_up_date')
    search_fields = ('customer_name', 'details')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'employee', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('title', 'message')