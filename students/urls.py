from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('add/', views.add_student, name = 'add_student'),
    path('students/', views.view_all, name = 'view_all'),
]