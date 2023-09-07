from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class FirstMail(models.Model):

    Email= models.EmailField(max_length=100)

    def __str__(self):
        return self.Email
    


class ContactTest(models.Model):

    Name= models.CharField(max_length=100)
    Email= models.EmailField(max_length=100)
    Phone= models.CharField(max_length=100)
    Service= models.CharField(max_length=100)
    Message= models.CharField(max_length=100)

    def _str_(self):
        return self.Name
    

class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    services = models.TextField()
    reach = models.CharField(max_length=20)
    hear = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
 