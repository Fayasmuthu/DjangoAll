from django.db import models

# Create your models here.

class form_oxdu(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    city=models.CharField(max_length=100)
    select=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
