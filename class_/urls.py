from django.urls import path
from .views import  ClassDetailView,requeststudent,classRemove,requestAccept,studentRemoveFromClass,stream,comment

urlpatterns = [
    path('details/<slug:slug>/',ClassDetailView.as_view(),name='class_details'),
    path('remove/<int:id>/',classRemove,name='class_remove'),
    path('request/student/<int:id>',requeststudent,name='class_student_request'),
    path('accept/<int:class_id>/<int:student_id>',requestAccept,name='requestAccept'),
    path('student/remove/<int:class_id>/<int:student_id>', studentRemoveFromClass, name='remove_student'),
    path('stream/',stream,name='stream_class'),
    path('comment/',comment,name='comment'),

]