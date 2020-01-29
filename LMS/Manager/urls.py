from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='manager_dashboard'),
    path('teachers_list/', views.teachers_list, name='teachers_list'),
    path('students_list/', views.students_list, name='students_list'),
    path('add_teacher_form/', views.add_teacher_form, name='add_teacher_form'),

]
