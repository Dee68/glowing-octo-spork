from django import forms
from django.db.models import fields
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['customer','address','city','state','zipcode']
        labels = {
            'customer':'',
            'address':'',
            'city':'',
            'state':'',
            'zipcode':''
        }
        
        forms.widgets = {
            'customer':forms.TextInput(attrs={'placeholder':'Enter UserName'}),
            'address':forms.TextInput(attrs={'placeholder':'Enter Address'}),
            'city':forms.TextInput(attrs={'placeholder':'Enter City'}),
            'state':forms.TextInput(attrs={'placeholder':'Enter State'}),
            'zipcode':forms.TextInput(attrs={'placeholder':'Enter Zipcode'}),
        }