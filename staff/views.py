from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from reports.models import SalesReport, FieldReport, CustomerReport, Notification
from staff.models import Employee


# 1. صفحة تسجيل الدخول
def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('staff:dashboard')
        else:
            error = "اسم المستخدم أو كلمة المرور غير صحيحة"
    
    return render(request, 'login.html', {'error': error})


# 2. لوحة التحكم
@login_required
def dashboard(request):
    try:
        employee = request.user.employee
        notifications = Notification.objects.filter(employee=employee, is_read=False).order_by('-created_at')
    except:
        employee = None
        notifications = []

    return render(request, 'dashboard.html', {
        'employee': employee,
        'notifications': notifications
    })


# 3. لوحة التحليلات (يجب أن تكون هنا بالضبط)
@login_required
def analytics_dashboard(request):
    # 1. إجمالي التقارير
    total_sales = SalesReport.objects.count()
    total_field = FieldReport.objects.count()
    total_customer = CustomerReport.objects.count()

    # 2. أفضل موظف في المبيعات
    top_sales_employee = SalesReport.objects.values(
        'employee__user__first_name', 'employee__user__last_name'
    ).annotate(count=Count('id')).order_by('-count').first()

    # 3. تحليل ملاحظات العملاء
    complaints = CustomerReport.objects.filter(issue_type='complaint').count()
    suggestions = CustomerReport.objects.filter(issue_type='suggestion').count()
    praises = CustomerReport.objects.filter(issue_type='praise').count()

    # 4. الإشعارات
    notifications_sent = Notification.objects.count()
    notifications_read = Notification.objects.filter(is_read=True).count()

    # 5. قائمة الموظفين
    employees = Employee.objects.all()

    context = {
        'total_sales': total_sales,
        'total_field': total_field,
        'total_customer': total_customer,
        'top_sales_employee': top_sales_employee,
        'complaints': complaints,
        'suggestions': suggestions,
        'praises': praises,
        'notifications_sent': notifications_sent,
        'notifications_read': notifications_read,
        'employees': employees,
    }

    return render(request, 'staff/analytics.html', context)