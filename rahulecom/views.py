from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from django.template import loader
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from .models import Register
from django.urls import reverse_lazy

# Create your views here.
def home(request):
   now = datetime.datetime.now()
   return render(request, "index.html", {"now" : now})
   
def register(request):
   now = datetime.datetime.now()
   return render(request, "register.html", {"now" : now})
   
class RegisterCreate(CreateView):
    model=Register
    fields = ['user_id', 'username', 'password','gender', 'number','email','location']
    template_name='register.html'
    success_url = ('/register')