from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('view/', views.view_students, name='view_students'),
    path('search/', views.search_student, name='search_student'),
    path('update/<int:admission_number>/', views.update_student, name='update_student'),
    path('delete/<int:admission_number>/', views.delete_student, name='delete_student'),
    path('topper/', views.topper, name='topper'),
]
