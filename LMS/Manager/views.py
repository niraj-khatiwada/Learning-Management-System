from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'Manager/dashboard.html')

def teachers_list(request):
    return render(request, 'Manager/Teacher Related/teachers_list.html')

def students_list(request):
    return render(request, 'Manager/Student Related/students_list.html')

def add_teacher_form(request):
    return render(request, 'Manager/Teacher Related/add_teacher_form.html')