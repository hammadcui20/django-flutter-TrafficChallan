from django import forms
from .models import ContactMessage
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
        'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'style': 'height: 150px'}),
    }

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Password'}))