from django.contrib import admin
from .models import Product,Carousel,Order,Orderitem

# Register your models here.
admin.site.register(Product)
admin.site.register(Carousel)
admin.site.register(Order)
admin.site.register(Orderitem)

