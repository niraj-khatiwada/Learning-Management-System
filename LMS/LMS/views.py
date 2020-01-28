from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView, ListView


class Home(TemplateView):
    template_name = 'home.html'

class Signin(View):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
   
class Signup(View):
    template_name = 'signup.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')