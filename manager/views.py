from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from .forms import ManagerForm
from account.models import Account
from .models import Manager
from lms.mail import Mail
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from teacher.models import Teacher
from student.models import Student
from lms.suspend import suspend_user, unsuspend_user
from django.core.cache import cache
from django.views.generic import DetailView
# Create your views here.


def randomPassword():
    password = ''
    letters = string.ascii_letters + string.digits + string.punctuation
    for i in range(10):
        password = password+str(random.choice(letters))
    return password


class FirstManager(View):
    template_name = 'manager/first.html'
    form = ManagerForm

    @method_decorator(login_required, 'signin')
    def get(self, request, *arg, **kwargs):
        try:
            a = Manager.objects.get(user_id=request.user.id)
            return redirect(reverse('manager_dashboard'))
        except:
            context = {
                'form': self.form()
            }
            return render(request, self.template_name, context)

    def post(self, request, *arg, **kwargs):
        myform = self.form(request.POST)
        if myform.is_valid():
            data = myform.save(commit=False)
            data.user_id = request.user.id
            data.save()
            user = Account.objects.get(id=request.user.id)
            user.is_firstLogin = False
            user.save()
            return redirect(reverse('manager_dashboard'))
        else:
            return render(request, self.template_name, {'form': myform})


class ManagerView(View):
    template_name = 'manager/dashboard.html'

    @method_decorator(login_required, 'signin')
    def get(self, request, *arg, **kwargs):
        if request.user.is_firstLogin:
            return redirect(reverse('first_manager'))
        else:
            return render(request, self.template_name)


class TeacherView(View):
    template_name = 'manager/teacher.html'

    @method_decorator(login_required, 'signin')
    def get(self, request, *arg, **kwargs):
        teacher = Teacher.objects.all()
        context = {
            'teacher': teacher
        }
        cache.clear()
        return render(request, self.template_name, context)

    @method_decorator(login_required, 'signin')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        name = request.POST.get('name')
        password_ = randomPassword()
        try:
            user = Account(email=email, password=make_password(
                password_), is_teacher=True)
            user.save()
            msg = f'{name}, Your account is created Please use the following credential to login into your account \n Email: {email} \n password: {password_}'
            Mail(subject="Account Creation",
                 message=msg, recipient_list=[email, ])
            teacher = Teacher(name=name, user_id=user.id)
            teacher.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Teacher Account is created successfully')
            return redirect(reverse('manage_teacher'))
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
            return redirect('manage_teacher')


class TeacherDetailsView(DetailView):
    model = Teacher


class StudentView(View):
    template_name = 'manager/student.html'

    @method_decorator(login_required, 'signin')
    def get(self, request, *arg, **kwargs):
        student = Student.objects.all()
        context = {
            'student': student
        }
        cache.clear()
        return render(request, self.template_name, context)

    @method_decorator(login_required, 'signin')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        name = request.POST.get('name')
        password_ = randomPassword()
        try:
            user = Account(email=email, password=make_password(
                password_), is_student=True)
            user.save()
            msg = f'{name}, Your account is created Please use the following credential to login into your account \n Email: {email} \n password: {password_}'
            Mail(subject="Account Creation",
                 message=msg, recipient_list=[email, ])
            student = Student(name=name, user_id=user.id)
            student.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Student Account is created successfully')
            return redirect('manage_student')
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
            return redirect('manage_student')


class StudentDetailsView(DetailView):
    model = Student


def delete_teacher(request, id):
    try:
        t = Account.objects.get(id=id)
        t.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully Delete')
        return redirect(reverse('manage_teacher'))
    except:
        messages.add_message(request, messages.ERROR, 'some error occured')
        return redirect(reverse('manage_teacher'))


def suspend_teacher(request, user_id):
    try:
        if suspend_user(user_id):
            messages.add_message(request, messages.SUCCESS,
                                 'successfully suspended')
        else:
            messages.add_message(
                request, messages.ERROR, 'could not suspend right now plase try again later')
        return redirect(reverse('manage_teacher'))
    except:
        messages.add_message(request, messages.ERROR,
                             'could not suspend right now plase try again later')
        return redirect(reverse('manage_teacher'))


def unsuspend_teacher(request, user_id):
    try:
        if unsuspend_user(user_id):
            messages.add_message(request, messages.SUCCESS,
                                 'successfully Released')
        else:
            messages.add_message(
                request, messages.ERROR, 'could not release right now plase try again later')
        return redirect(reverse('manage_teacher'))
    except:
        messages.add_message(request, messages.ERROR,
                             'could not release right now plase try again later')
        return redirect(reverse('manage_teacher'))


def delete_student(request, id):
    try:
        t = Account.objects.get(id=id)
        t.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully Delete')
        return redirect(reverse('manage_student'))
    except:
        messages.add_message(request, messages.ERROR, 'some error occured')
        return redirect(reverse('manage_student'))


def suspend_student(request, user_id):
    try:
        if suspend_user(user_id):
            messages.add_message(request, messages.SUCCESS,
                                 'successfully suspended')
        else:
            messages.add_message(
                request, messages.ERROR, 'could not suspend right now plase try again later')
        return redirect(reverse('manage_student'))
    except:
        messages.add_message(request, messages.ERROR,
                             'could not suspend right now plase try again later')
        return redirect(reverse('manage_student'))


def unsuspend_student(request, user_id):
    try:
        if unsuspend_user(user_id):
            messages.add_message(request, messages.SUCCESS,
                                 'successfully Released')
        else:
            messages.add_message(
                request, messages.ERROR, 'could not release right now plase try again later')
        return redirect(reverse('manage_student'))
    except:
        messages.add_message(request, messages.ERROR,
                             'could not release right now plase try again later')
        return redirect(reverse('manage_student'))
