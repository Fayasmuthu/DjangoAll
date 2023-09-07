from django.db import models

# Create your models here.
class form(models.Model):
    name=models.CharField(max_length=150)
    Date=models.CharField(max_length=50)
    email=models.EmailField()
    moblie=models.IntegerField()
    gender=models.GenericIPAddressField (max_length=50)
    occupation=models.CharField(max_length=50)
    ID_type=models.CharField(max_length=50)
    ID_number=models.IntegerField()
    Issue_Authority=models.CharField(max_length=50)
    Issue_Date=models.CharField(max_length=50)
    Issue_State=models.CharField(max_length=50)
    Expliry_Date=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

    

