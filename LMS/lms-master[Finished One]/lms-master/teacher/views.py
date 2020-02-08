from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from class_.forms import ClassForm
import random
import string
from class_.models import Class
from django.contrib import messages
from teacher.models import Teacher
# Create your views here.

def randomcode():
    code = ''
    letters = string.ascii_letters + string.digits
    for i in range(5):
        code=code+str(random.choice(letters))
    return code

def checkcode(code):
    try:
        Class.objects.get(code=code)
        return True
    except:
        return False

def getLoginTeacherId(user_id):
    t = Teacher.objects.get(user_id=user_id)
    return t.id


class TeacherView(View):
    template_name = 'teacher/dashboard.html'
    form_class = ClassForm

    @method_decorator(login_required,'signin')
    def get(self,request,*args,**kwargs):
        context = {
            'form':self.form_class(),
            'class':Class.objects.filter(teacher_id=getLoginTeacherId(request.user.id)),
            'teacher':Teacher.objects.get(id=getLoginTeacherId(request.user.id))
        }
        if request.user.is_firstLogin:
            return redirect('password_change')
        else:
            return render(request,self.template_name,context)

    def post(self,request,*arg,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            code = randomcode()
            isvalidcode = checkcode(code)
            while isvalidcode:
                code = randomcode()
                isvalidcode = checkcode(code)
            data.code = code
            data.teacher_id = getLoginTeacherId(request.user.id)
            data.save()
            messages.add_message(request,messages.SUCCESS,'successfully created')
            return redirect('teacher_dashboard')
        else:
            messages.add_message(request,messages.ERROR,'sorry could not create right now')
            return redirect('teacher_dashboard')

