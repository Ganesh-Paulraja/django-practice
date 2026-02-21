from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from.forms import MyForm
from .models import*

def index(request):
    return HttpResponse("welcome to my page !")

def home(request):
    title = "Ganesh Dev"
    courses = ['php', 'java', 'dotnet', 'python']
    details = { 'name': 'ajin',
               'address': 'IN'
            }
    return render(request, 'home.html', {'title': title, 'courses': courses, 'details': details})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')






# def register(request):
#     if request.method=="POST":
#         form=MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Data send successfully !")
    
#     else:
#         form=MyForm()
#         return(request,'register.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        
        if form.is_valid():
            form.save()
        return HttpResponse("Data sent successfully!")

    else:
        form = MyForm()   # create empty form for GET request

        return render(request, 'register.html', {'form': form})
    

def insert(request):
    if request.method == "POST":

        name=request.POST['name']
        address=request.POST['address']
        price=request.POST['price']
        data=MyClass.objects.create(name=name,address=address,price=price)
        data.save()
        return HttpResponse("Data sent successfully!")
    else:
        return render(request,'insert.html')
    


def show(request):
    data=MyClass.objects.all()
    return render(request,'show.html',{'data':data})