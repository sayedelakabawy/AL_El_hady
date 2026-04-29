from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),             # الصفحة الرئيسية
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expenses/', views.expenses, name='expenses'), #اللينك بتاع الصفح هنا
]