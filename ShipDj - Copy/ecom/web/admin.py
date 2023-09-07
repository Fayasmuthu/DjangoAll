from django.contrib import admin
from . models import FirstMail,ContactTest,QuoteRequest


# Register your models here.
admin.site.register(FirstMail)
@admin.register(ContactTest)
class ContactTestAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Service','Message')
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display=('name','company','email','phone','services','message')



    



