from django.urls import path
from . import views

urlpatterns = [
    path('', views.workers, name='workers'),
    #path('search_workers/', views.Serch.as_view, name='search_workers'),
    #path('create/', views.create),
    path('create/', views.CreateWorker.as_view(), name='create_worker'),
    path('create_pos/', views.create_pos),
    #path('edit/<int:id>/', views.edit),
    path('edit/<int:id>/', views.Edit.as_view(), name='edit_worker'),
    path('delete/<int:id>/', views.delete),
    path('tabel/<int:id>/', views.tabel),
]