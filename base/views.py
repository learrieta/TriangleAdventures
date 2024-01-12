from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def tours(request):
    return render(request, 'base/tours.html')

def two_hour(request):
    return render(request, 'base/twohour.html')
def three_hour(request):
    return render(request, 'base/threehour.html')
def four_hour(request):
    return render(request, 'base/fourhour.html')

def faq(request):
    return render(request, 'base/faq.html')
def how(request):
    return render(request, 'base/how_it_works.html')
def who(request):
    return render(request, 'base/who_we_are.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_from = settings.EMAIL_HOST_USER


            EmailMessage(
                'Contact Form Submission from {}'.format(first_name),
                message,
                email_from,
                ['hid21002@byui.edu'],
                [],
                reply_to=[email] 
            ).send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'base/contactus.html', {'form' : form})


def success(request):
    return render(request, 'base/success.html')