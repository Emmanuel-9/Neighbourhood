from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django import forms



class SignUpForm(UserCreationForm):    

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2'] 

class UserUpdateForm(ModelForm):
    email = forms.EmailField(max_length=150)


    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):
    bio = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['image', 'bio', 'neighbourhood']