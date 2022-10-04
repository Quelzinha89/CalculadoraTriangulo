from django.urls import path
from . import views

urlpatterns = [
    path('<catetoA>&<catetoB>/', views.home),
    path('', views.home),
]