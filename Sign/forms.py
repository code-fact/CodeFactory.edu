from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class profile(UserChangeForm):
    username = forms.TextInput(attrs={'class':'form-control'})
    first_name = forms.TextInput(attrs={'class':'form-control'})
    last_name = forms.TextInput(attrs={'class':'form-control'})
    email = forms.EmailInput(attrs={'class':'form-control'})
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
