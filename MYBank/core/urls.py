from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="index"),
    path('about/', about, name="about"),
    path('view_customer/<int:id>/', view_customer, name="view_customer"),
    path('transfer/', transfer, name="transfer"),
    path('make_transaction/<int:id>', make_transaction, name="make_transaction"),
    path('contact/', contact, name="contact"),
    path('view_all_customers/', view_all_customers, name="view_all_customers"),
    path('services', services, name="services")
]
