from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('show/', views.show, name='show'),
    path('update/<int:id>', views.item_update, name='update'),
    path('delete/<int:id>', views.item_delete, name='delete'),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('login/', views.login_view, name="login"),
]