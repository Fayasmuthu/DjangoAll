from django.shortcuts import render,redirect
from .models import Ch_Product,Ch_Slider
from .models import Contact
import requests

# Create your views here.

def index(request):
    card_form = Ch_Product.objects.all()
    slide_chocolux =Ch_Slider.objects.all()
    context={
        'card':card_form,
        'slider':slide_chocolux
    }

    if request.method == 'POST':
        full_name = request.POST.get('fname')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the database
        contact = Contact.objects.create(
            full_name=full_name, 
            phone_number=phone_number, 
            email=email, 
            message=message
            )
        contact.save()

        # Send WhatsApp message using a WhatsApp API (Twilio API in this example)
        # Replace ACCOUNT_SID, AUTH_TOKEN, and FROM_PHONE_NUMBER with your Twilio account details
        ACCOUNT_SID = 'your_account_sid_here'
        AUTH_TOKEN = 'your_auth_token_here'
        FROM_PHONE_NUMBER = 'your_twilio_phone_number_here'
        TO_PHONE_NUMBER = '+91 6282134481'  # Replace with the desired recipient phone number

        base_url = "https://api.twilio.com/2010-04-01/Accounts/{0}/Messages.json"
        url = base_url.format(ACCOUNT_SID)
        payload = {
            "From": FROM_PHONE_NUMBER,
            "To": TO_PHONE_NUMBER,
            "Body": f"New Message from {full_name}\n\nEmail: {email}\nPhone: {phone_number}\n\n{message}"
        }
        auth = (ACCOUNT_SID, AUTH_TOKEN)

        response = requests.post(url, data=payload, auth=auth)

        if response.status_code == 201:
            # Redirect to a success page if the message was sent successfully
            return redirect('success_page')
        else:
            # Handle the error case appropriately (e.g., show an error page or return an error message)
            return render(request, 'error.html')

    return render(request, "index.html",context)




# def register_view(request):
#     if request.method == 'POST':
#         form = YourFormNameForm(request.POST)
#         if form.is_valid():
#             # Process the valid form data, e.g., save it to the database
#             name = form.cleaned_data['name']
#             age = form.cleaned_data['age']
#             # ... do something with name and age ...
#             user_profile = UserProfile(
#                 name=name,
#                 age=age) 
#             user_profile.save()
#     else:
#         form = YourFormNameForm()

#     return render(request, 'registration_template.html', {'form': form})

def login_view(request):
    return render(request,'registration/login.html')


def send_whatsapp_message(request):
    if request.method == 'POST':
        full_name = request.POST.get('fname')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the database
        contact = Contact.objects.create(
            full_name=full_name, 
            phone_number=phone_number, 
            email=email, 
            message=message
            )
        contact.save()

        # Send WhatsApp message using a WhatsApp API (Twilio API in this example)
        # Replace ACCOUNT_SID, AUTH_TOKEN, and FROM_PHONE_NUMBER with your Twilio account details
        ACCOUNT_SID = 'your_account_sid_here'
        AUTH_TOKEN = 'your_auth_token_here'
        FROM_PHONE_NUMBER = 'your_twilio_phone_number_here'
        TO_PHONE_NUMBER = '+1234567890'  # Replace with the desired recipient phone number

        base_url = "https://api.twilio.com/2010-04-01/Accounts/{0}/Messages.json"
        url = base_url.format(ACCOUNT_SID)
        payload = {
            "From": FROM_PHONE_NUMBER,
            "To": TO_PHONE_NUMBER,
            "Body": f"New Message from {full_name}\n\nEmail: {email}\nPhone: {phone_number}\n\n{message}"
        }
        auth = (ACCOUNT_SID, AUTH_TOKEN)

        response = requests.post(url, data=payload, auth=auth)

        if response.status_code == 201:
            # Redirect to a success page if the message was sent successfully
            return redirect('success_page')
        else:
            # Handle the error case appropriately (e.g., show an error page or return an error message)
            return render(request, 'error.html')

    return render(request, 'whatsapp_form.html')
