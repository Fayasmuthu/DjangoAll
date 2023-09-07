from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    context={
        'prod':Product.objects.all()
    }
    return render(request,"web/index.html",context)

def fashion1(request):
    return render(request,"web/fashion.html")