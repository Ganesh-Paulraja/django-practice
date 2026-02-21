from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from.forms import MyForm
from .models import*

def index(request):
    return HttpResponse("welcome to my page !")

def home(request):
    title = "Jclick Solution"
    course = ['php', 'java', 'dotnet', 'python']
    detail = {'name': 'Ajin', 'address': 'IN'}
    return render(request, 'home.html', {'title': title, 'courses': course, 'details': detail})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        
        if form.is_valid():
            form.save()
        return HttpResponse("Data sent successfully!")

    else:
        form = MyForm()   # create empty form for GET request

        return render(request, 'register.html', {'form': form})