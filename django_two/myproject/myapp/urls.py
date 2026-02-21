from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('show/', views.show, name='show'),
]