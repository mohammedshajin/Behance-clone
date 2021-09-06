from django.urls import path
from . import views

urlpatterns = [
    path('', views.userAccount, name='profile'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('edit-account', views.editAccount, name='edit-account'),
    path('profile/<str:pk>/', views.profile, name='other_profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.viewmessage, name='message'),
    path('send-message/<str:pk>/', views.createmessage, name='create-message'),
    path('follow/<str:pk>/', views.follow, name='follow'),
    path('unfollow/<str:pk>/', views.unfollow, name='unfollow'),
    ]