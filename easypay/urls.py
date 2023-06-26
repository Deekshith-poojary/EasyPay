from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.details, name='details'),    
    path('payment', views.payment, name='payment'),
    path('getdata', views.getdata, name='getdata'),
]