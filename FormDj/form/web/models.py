from django.db import models

# Create your models here.

class form_data(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    