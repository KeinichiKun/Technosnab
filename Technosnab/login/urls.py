from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LogView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterUserView.as_view(), name='register')
]