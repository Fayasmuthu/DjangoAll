from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"web/index.html")
def login1(request):
    return render(request,"web/account/login.html")