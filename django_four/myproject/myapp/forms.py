from django import forms
from .models import MyClass

class MyForm(forms.ModelForm):
    class Meta:
        model = MyClass
        fields = ['name', 'address', 'price'] # or '__all__
