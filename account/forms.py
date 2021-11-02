from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import widgets
from django import forms
from .models import UserProfile

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


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']   
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email.'}),
        'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name.'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
    }

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1', 'new_password2'] 
        labels = {
            'old_password':'Old Password',
            'new_password1':'New Password',
            'new_password2':'Confirm Password'
        }
        widgets = {
            'old_password':forms.PasswordInput(attrs={'class':'form-control','autocomplete':True,'required':'required'}),
            'new_password1':forms.PasswordInput(attrs={'class':'form-control', 'required':'required'}),
            'new_password2':forms.PasswordInput(attrs={'class':'form-control','required':'required'})
        }   

City = (
    ('Abuja','Abuja'),
    ('Lagos','Lagos'),
    ('Kaduna','Kaduna'),
    ('Port-harcourt','Port-harcourt'),
    ('Yenegoa','Yenegoa'),
    ('Kano','Kano'),
    ('Sokoto','Sokoto'),
)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','city','country','company','image']
        widgets = {
        'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'your phone'}),
        'address':forms.TextInput(attrs={'class':'form-control','placeholder':'your address here.'}),
        'city': forms.Select(attrs={'class':'form-control','placeholder':'your city here.'}, choices=City),
        'country':forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),
        'company':forms.TextInput(attrs={'class':'form-control','placeholder':'Your company'}),
        'image': forms.FileInput(attrs={'class':'form-control','placeholder':'upload your avatar'})
         }
