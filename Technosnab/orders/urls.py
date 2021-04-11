from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),


    path('edit/<int:id>/', views.OrderEdit.as_view(), name='edit_order'),

    path('create/', views.OrderCreate.as_view(), name='create_order'),

    path('create/create_cust/', views.CreateCustomer.as_view(), name='cust_create'),


    path('delete/<int:id>/', views.delete),
    path('complite/<int:id>/', views.complite, name='complite'),
]