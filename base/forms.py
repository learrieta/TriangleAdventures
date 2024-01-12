from django import forms
from django.contrib.auth.forms import User

from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    
    message = forms.CharField(widget=forms.Textarea)

    class Meta():
        fields = ('first_name','last_name','email','message')
