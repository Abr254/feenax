from django.urls import path
from . import views

urlpatterns = [
    path('', views.withdrawal, name='withdrawal'),
    path('admin/check_balance', views.withdrawal, name='check_balance'),
]