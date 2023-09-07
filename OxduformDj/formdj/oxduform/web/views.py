from django.shortcuts import render
from . models import form_oxdu

# Create your views here.

def index (request):
    if request.method=="POST":
        name=request.POST.get("name_1")
        phone=request.POST.get("phone_1")
        city=request.POST.get("city_1")
        select=request.POST.get("select_1")

        form_1=form_oxdu(
            name=name,
            phone=phone,
            city= city,
            select=select,

        )
        form_1.save()

    return render(request,("web/index.html"))