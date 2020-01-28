from django.shortcuts import render,redirect
from django.contrib import messages
from Account.models import Account

from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate

def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email_ = request.POST.get("email")
        password_ = request.POST.get("password")
        user = authenticate(email = email_, password = password_)
        if user is not None:
            login(request, user)
            if request.user.is_manager:
                return render(request, 'Manager/dashboard.html')
            elif request.user.is_teacher:
                return render(request, 'Teacher/dashboard.html')
            elif request.user.is_student:
                return render(request, 'Student/dashboard.html')
            else:
                messages.error(request, 'There was some problem. Please log in again')
                return redirect('login')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')


    

def signup(request):
    return render(request, 'signup.html')   
