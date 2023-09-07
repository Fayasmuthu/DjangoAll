from django.shortcuts import render
from .models import form_data

# Create your views here.

def index(request):
    
    if request.method=="POST":
        name=request.POST.get("name_1")
        age=request.POST.get("age_1")
        email=request.POST.get("email_1")
        phone=request.POST.get("number_1")

        form_1=form_data(
            name=name,
            age=age,
            email=email,
            phone=phone
        )
        form_1.save()

    return render(request,"web/index.html")