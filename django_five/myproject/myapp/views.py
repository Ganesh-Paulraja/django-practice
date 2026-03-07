from django.shortcuts import render
from django.http import HttpResponse
from.forms import MyForm
from .models import*
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
    
def show(request):
    data=MyClass.objects.all()
    return render(request,'show.html',{'data':data})

def item_update(request, id):
    data = get_object_or_404(MyClass, id = id)
    if request.method == "POST":
        form = MyForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = MyForm(instance = data)
        return render(request, 'update.html', {'form': form})
    
def item_delete(request, id):
    data = get_object_or_404(MyClass, id = id)
    if request.method == 'POST':
        data.delete()
        return redirect('show')
    else:
        return render(request, 'delete.html', {'data': data})
    

#login,logout default parameters
#auth_user default db will used becuse of User
#atlesaset one time make mibration
# auto hashing 

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        data = User.objects.create(username=username, password=password)
        data.save()
        return HttpResponse("Data Send Successfully")
    else: 
        return render(request, 'signin_reg.html') #it rendurs form after post if block


#import
# from django.contrib import messages
# from django.contrib import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
      username = request.POST.get('name')
      password = request.POST.get('password')
      data = authenticate(username = username, password = password)

      if data is not None:
        login(request, data)
        messages.success(request, "Login Successfully")
        return redirect('login')
    else:
        return render(request, 'login_reg.html')