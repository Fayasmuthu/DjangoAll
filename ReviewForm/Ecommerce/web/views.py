from django.shortcuts import render
from . models import form

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        Date=request.POST.get("Date")
        email=request.POST.get("email")
        moblie=request.POST.get("moblie")
        gender=request.POST.get("gender")
        occupation=request.POST.get("occupation")
        ID_type=request.POST.get("ID_type")
        ID_number=request.POST.get("ID_number")
        Issue_Authority=request.POST.get("Issue_Authority")
        Issue_Date=request.POST.get("Issue_Date")
        Issue_State=request.POST.get("Issue_State")
        Expliry_Date=request.POST.get("Expliry_Date")


        form_1=form(
            name=name,
            Date=Date,
            email=email,
            moblie=moblie,
            gender=gender,
            occupation=occupation,
            ID_type=ID_type,
            ID_number=ID_number,
            Issue_Authority=Issue_Authority,
            Issue_Date=Issue_Date,
            Issue_State=Issue_State,
            Expliry_Date=Expliry_Date

        )
        form_1.save()
    return render (request,"web/index.html")