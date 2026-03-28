from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import MyForm, UploadForm
from .models import*
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#import for send mails
from django.core.mail import send_mail

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
        return render(request, 'update_data.html', {'form': form})
    
def item_delete(request, id):
    data = get_object_or_404(MyClass, id = id)
    if request.method == 'POST':
        data.delete()
        return redirect('show')
    else:
        return render(request, 'delete.html', {'data': data})

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        data = User.objects.create_user(username=username, password=password)
        data.save()
        return HttpResponse("Data Send Successfully")
    else: 
        return render(request, 'signin_reg.html') #it rendurs form after post if block
    
def login_view(request):
    if request.method == "POST":
      username = request.POST.get('name')
      password = request.POST.get('password')
      data = authenticate(username = username, password = password)

      if data is not None:
        login(request, data)
        messages.success(request, "Login Successfully")
        return redirect('login_reg')
    else:
        return render(request, 'login_reg.html')


def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        return HttpResponse("Data sent successfully!")

    else:
        form = UploadForm()   # create empty form for GET request

        return render(request, 'upload.html', {'form': form})
    
def show_files(request):
    files= upload.objects.all()
    return render(request,'file_show.html',{'files':files})

def send_email_view(request):
    if request.method == "POST":
        #get data from the form
        username = request.POST.get('name')
        subject = request.POST.get('subject')
        messages = request.POST.get('message')
        recipient = request.POST.get('recipient')
        try:
            send_mail(
                subject= subject,
                message= messages,
                from_email="ganeshsgk4@gmail.com",
                recipient_list=['ganeshsgk4@gamil.com'],
                fail_silently= False,
            )
            send_mail(
                subject=f"hi {username} thanks for visit my website",
                message= messages,
                #from _email = "your_eamil@gmail.com",
                from_email="ganeshsgk4@gmail.com", # Replace with your email
                #Replace with your email
                recipient_list=[recipient],
                #fail_silently=False,
            )
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")
        
    
    return render(request, 'mail_me.html')

