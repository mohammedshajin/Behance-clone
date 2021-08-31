from django.urls import path
from . import views

urlpatterns = [
    path('', views.work, name='work'),
    path('worksingle/<str:pk>/', views.work_single, name="work_single")
]
