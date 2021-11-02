from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import widgets
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'password1Field','value':"{{ fieldVals.username}}"}),
            'email':forms.EmailInput(attrs={'class':'text email','name':'email','id':'emailField','placeholder':'Email','value':"{{ fieldVals.email }}"}),
            'password1': forms.PasswordInput(attrs={'class':'text','id':'password1Field','placeholder':'Password','name':'password1'}),
            'password2':forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'})
        }
