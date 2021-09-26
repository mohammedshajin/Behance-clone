from django.urls import path

from .import views

urlpatterns = [
    path('', views.getRoutes),
    path('works/', views.getWorks),
    path('works/<str:pk>/', views.getWork),
    ]