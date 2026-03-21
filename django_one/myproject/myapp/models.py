from django.db import models

# Create your models here.

class MyClass(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
   
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
    


class upload(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/files') #for general files
    image = models.ImageField(upload_to = 'uploads/images') #For images

    def __str__(self):
        return self.name
    