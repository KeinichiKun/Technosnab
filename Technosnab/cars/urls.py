from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),

    #path('search_car/', views.Serch.as_view(), name='search_car'),


   # path('create/', views.create),
    path('create/', views.CreateCar.as_view(), name='create_car'),
    #path('detail/<int:id>/', views.edit, name='detail_car'),
    path('detail/<int:id>/', views.DetailCar.as_view(), name='detail_car'),
    path('delete/<int:id>/', views.delete),


   # path('detail/<int:id>/createpr/', views.create_profit),

    #path('detail/<int:id>/createex/', views.create_expenses),
    path('detail/<int:id>/createex/', views.create_expenses),
    # path('editEx/<int:id>', views.editEx, name='editEx'),
    path('deleteEx/<int:id>', views.deleteEx, name='deleteEx'),


    path('detail/createrep/<int:id>', views.create_rep, name='createRep'),
    path('deleteRep/<int:id>/', views.deleteRep, name='deleteRep'),


]