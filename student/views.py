from django.shortcuts import render, redirect, reverse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from class_.models import Class, ClassJoined
from django.db.models import Q
from .models import Student
from django.contrib import messages
# Create your views here.


def getLogedInStudentId(user_id):
    s = Student.objects.get(user_id=user_id)
    return s.id


class StudentView(View):
    template_name = 'student/dashboard.html'

    @method_decorator(login_required, 'signin')
    def get(self, request, *args, **kwargs):
        all_id = [x.class_join_id for x in ClassJoined.objects.filter(
            student_id=getLogedInStudentId(request.user.id), is_accept=True)]
        all_class = Class.objects.filter(id__in=all_id)
        if request.user.is_firstLogin:
            return redirect(reverse('password_change'))
        else:
            return render(request, self.template_name, {'class': all_class})


def searchclass(reqeust):
    if reqeust.method == 'GET':
        key = reqeust.GET.get('key')
        s = Class.objects.filter(Q(name__contains=key) | Q(code=key))
        c = ClassJoined.objects.filter(student_id=getLogedInStudentId(
            reqeust.user.id)).only('class_join_id')
        class_id = [x.id for x in c]
        context = {
            'result': s,
            'key': key,
            'class_id': class_id,
        }
        return render(reqeust, 'student/search.html', context)
    else:
        return redirect(reverse('student_dashbaord'))


login_required(login_url='signin')


def classJoin(request, class_id):
    if request.method == 'GET':
        try:
            c = ClassJoined()
            c.student_id = getLogedInStudentId(request.user.id)
            c.class_join_id = class_id
            c.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your request to join the class has been sent')
            return redirect(reverse('student_dashbaord'))
        except Exception as e:
            messages.add_message(
                request, messages.ERROR, 'sorry we could not sent your request right now : '+str(e))
            return redirect(reverse('student_dashbaord'))
    else:
        return redirect(reverse('student_dashbaord'))
