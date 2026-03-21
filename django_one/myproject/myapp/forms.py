from django import forms
from .models import *

class MyForm(forms.ModelForm):
    class Meta:
        model = MyClass
        fields = ['name', 'address', 'price'] # or '__all__

class UploadForm(forms.ModelForm):
    class Meta:
        model = upload
        fields = ['name', 'file', 'image'] # or '__all__