from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics_dashboard, name='analytics'),
]