from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models  import message

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email'] 

class MessageForm(forms.ModelForm):
    class Meta:
        model=message
        fields='__all__'