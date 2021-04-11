from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    # path('create/', views.create),
    path('create/', views.ServiceCreate.as_view(), name='create_product'),
    # path('edit/<int:id>/', views.edit),
    path('edit/<int:id>/', views.Edit.as_view(), name='edit_product'),
    path('delete/<int:id>/', views.delete),
]