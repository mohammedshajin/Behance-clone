from django.urls import path
from . import views

urlpatterns = [
    path('', views.userAccount, name='profile'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('edit-account', views.editAccount, name='edit-account')
    ]