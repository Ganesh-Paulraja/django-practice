from django.urls import path
from .import views


urlpatterns = [
    # path('index/', views.index),
    path('apilist/', views.data_list, name='list'),
]

# API

