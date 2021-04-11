from django.urls import path
from . import views

urlpatterns = [

    path('', views.customers, name='customers'),
    #
    # path('create/', views.create),
    # path('edit/<int:id>/', views.edit),
    path('create/', views.Create.as_view(), name='create_customer'),

    path('statistics/<int:id>/', views.statistics, name='statistics'),

    path('edit/<int:id>/', views.Edit.as_view(), name='edit_customer'),
    path('delete/<int:id>/', views.delete),

]