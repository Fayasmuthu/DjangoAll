from django.db import models

# Create your models here.

class Ch_Product(models.Model):
    image = models.ImageField(upload_to='Cho_card/img')
    name = models.CharField(max_length=100)
    last =models.CharField(max_length=100)
    price =models.IntegerField()

class Ch_Slider(models.Model):
    name =models.CharField(max_length=50)
    image =models.ImageField(upload_to='Slider/img')
    decoration =models.TextField(max_length=500)



class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
