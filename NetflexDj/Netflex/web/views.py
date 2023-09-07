from django.shortcuts import render

# Create your views here.
# function

def index(request):
    return render(request,"web/index.html")