from django.urls import path
from . import views

urlpatterns = [
    path('', views.work, name='work'),
    path('worksingle/<str:pk>/', views.work_single, name="work_single"),
    path('creatework/', views.creatework, name='creatework'),
    path('updatework/<str:pk>/', views.updatework, name="updatework"),
    path('deletework/<str:pk>/', views.deletework, name="deletework"),
    path('search/', views.search, name="search"),
    path('appreciate/<str:pk>/', views.appreciate, name="appreciate"),
]
