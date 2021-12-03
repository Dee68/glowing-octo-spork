from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import TextInput, Textarea, Widget
from . models import ContactMessage,SubscribedUser, MailMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email','subject','message']
        labels = {
            'name':'',
            'email':'',
            'subject':'',
            'message':''
        }
        
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control','id':'fname','placeholder':'Your fullname'}),
        'email':forms.TextInput(attrs={'class':'form-control','id':'email','placeholder':'Your email address'}),
        'subject':forms.TextInput(attrs={'class':'form-control','id':'subject','placeholder':'Your subject of this message'}),
        'message':forms.Textarea(attrs={'class':'form-control','id':'message','placeholder':'Your message','rows':8})
    }
    
class SubscribersForm(forms.ModelForm):
    class Meta:
        model = SubscribedUser
        fields = ['email']
        labels ={
            'email':''
        }
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email','required':'required'})
            
        }

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = ['subject','message','send_it']
        # widgets = {
        #     'subject':forms.TextInput(attrs={'class':'form-control'}),
        #     'message': forms.TextInput(attrs={'class':'form-control'}),
        #     'attachement':forms.FileInput(attrs={'class':'form-control'}),
        #     'subscribers': forms.MultipleChoiceField(choices=SubscribedUser.objects.all(), to_field_name='subscribers'),
        #     'send_it': forms.CheckboxInput(attrs={'class':'form-control'})
        # }