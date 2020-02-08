from . import views
from django.urls import path
from .views import (TeacherView
                    )
urlpatterns = [
    path('dashboard/',TeacherView.as_view(),name='teacher_dashboard'),
]
