from django.contrib import admin
from .models import Ch_Product,Ch_Slider,Contact

# Register your models here.
admin.site.register(Ch_Product)
admin.site.register(Ch_Slider)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'email', 'message']

admin.site.register(Contact, ContactAdmin)