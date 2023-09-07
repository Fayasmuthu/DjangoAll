from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    context={
        'prod' : product.objects.all(),
    }
    return render(request,"web/index.html",context)