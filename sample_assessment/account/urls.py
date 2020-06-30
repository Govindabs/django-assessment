from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path(r'users', views.users, name='users'),
    path(r'admin', views.admin, name='admin'),
    path(r'update/<int:pk>/', views.update_status, name='update_status'),
    path(r'pie_chart/', views.pie_chart, name='pie_chart'),
]
