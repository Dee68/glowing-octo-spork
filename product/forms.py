from django import forms
from django import forms
from django.forms import widgets
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address','city','state','zipcode']
        labels = {
            'address':'',
            'city':'',
            'state':'',
            'zipcode':''
        }
        
        widgets = {
            'address':forms.TextInput(attrs={'placeholder':'Enter Address','address':'address'}),
            'city':forms.TextInput(attrs={'placeholder':'Enter City','city':'city'}),
            'state':forms.TextInput(attrs={'placeholder':'Enter State','state':'state'}),
            'zipcode':forms.TextInput(attrs={'placeholder':'Enter Zipcode','zipcode':'zipcode'}),
        }