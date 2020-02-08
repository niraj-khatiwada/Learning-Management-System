from . import views
from django.urls import path
from .views import (FirstManager,
                    ManagerView,
                    TeacherView,
                    suspend_teacher,
                    unsuspend_teacher,
                    suspend_student,
                    unsuspend_student,
                    delete_teacher,
                    delete_student,
                    TeacherDetailsView,
                    StudentView,
                    StudentDetailsView
                    )
urlpatterns = [
    path('manager-first',FirstManager.as_view(),name='first_manager'),
    path('dashboard/',ManagerView.as_view(),name='manager_dashboard'),
    path('teacher/',TeacherView.as_view(),name='manage_teacher'),
    path('teacher/<int:pk>',TeacherDetailsView.as_view(),name='teacher_details'),
    path('teacher/suspend/<int:user_id>',suspend_teacher,name='suspend_teacher'),
    path('teacher/unsuspend/<int:user_id>',unsuspend_teacher,name='unsuspend_teacher'),
    path('teacher/remove/<int:id>',delete_teacher,name='delete_teacher'),
    path('student/', StudentView.as_view(), name='manage_student'),
    path('student/suspend/<int:user_id>',suspend_student,name='suspend_student'),
    path('student/unsuspend/<int:user_id>',unsuspend_student,name='unsuspend_student'),
    path('student/remove/<int:id>',delete_student,name='delete_student'),
    path('student/<int:pk>',StudentDetailsView.as_view(),name='student_details'),
]
