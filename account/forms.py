from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import widgets
from django import forms
from .models import UserProfile

class RegisterUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=100,required=True)
    # last_name = forms.CharField(max_length=100,required=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'text','placeholder':'Username','name':'username','id':'usernameField','value':"{{ fieldVals.username}}"}),
            'first_name':forms.TextInput(attrs={'class':'text','placeholder':'Firstname','name':'firstname','id':'firstnameField','value':"{{ fieldVals.firstname}}"}),
            'last_name':forms.TextInput(attrs={'class':'text','placeholder':'Lastname','name':'lastname','id':'lastnameField','value':"{{ fieldVals.lastname}}"}),
            'email':forms.EmailInput(attrs={'class':'text email','name':'email','id':'emailField','placeholder':'Email','value':"{{ fieldVals.email }}"}),
            'password1': forms.PasswordInput(attrs={'class':'text','id':'password1Field','placeholder':'Password','name':'password1'}),
            'password2':forms.PasswordInput(attrs={'class':'text w3lpass','name':'password2','id':'password2Field','placeholder':'Confirm Password'})
        }

    # def clean_first_name(self, *args, **kwargs):
    #     first_name = self.cleaned_data.get("first_name")
    #     if self.cleaned_data['first_name'].strip() == '':
    #         raise forms.ValidationError("First name is required.")
    #     return first_name

    # def clean_last_name(self, *args, **kwargs):
    #     last_name = self.cleaned_data.get("last_name")
    #     if len(last_name) == 0:
    #         raise forms.ValidationError("Last name is required.")
    #     return last_name

    # def save(self, commit=True):
    #     user = super(RegisterUserForm,self).save(commit=True)
    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.password = self.cleaned_data['password1']
    #     if commit:
    #         user.save()
    #     return user

        


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']   
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email.'}),
        # 'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name.'}),
        # 'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
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
