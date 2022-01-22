from django.db.models import query
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm,SubscribersForm
from . models import ContactMessage, Setting, SubscribedUser
from product.models import *
from account.models import UserProfile
from django_pandas.io import read_frame
from django.views.generic import ListView
# Create your views here.
def home(request):
    pictures = Picture.objects.filter(title__contains='slider')
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    setting = Setting.objects.get(pk=1)
    # userprofile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == "POST":
        form = SubscribersForm(request.POST)
        if form.is_valid():
            data = SubscribedUser()
            data.email = form.cleaned_data['email']
            #data.save(commit=False)#don't save yet to db
            if SubscribedUser.objects.filter(email = data.email).exists():
                messages.warning(request,'This email already exists in our database.')
                return HttpResponseRedirect("/")
            else:
            
                data.save()# save to database
            messages.success(request,'Subscription successful')
            return HttpResponseRedirect("/")
    else:
        form = SubscribersForm() 
    context = {'form':form,'products':products, 'pictures':pictures, 
    'pcategories':pcategories,'setting':setting}
    return render(request, 'home/index.html', context)


# contact page
def contactUs(request):
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    setting = Setting.objects.get(pk=1)
    # userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":# check for button click
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()# creates relation with model
            data.name = form.cleaned_data['name']# form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR') 
            data.save()# save to db
            messages.success(request,"Message successfully sent, we will get back to you soon.")
            return HttpResponseRedirect('/contact')
    form = ContactForm
    context = {'form':form,'products':products,'pcategories':pcategories,
    'setting':setting}
    return render(request, 'home/contact.html', context)

# about us page
def aboutUs(request):
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    setting = Setting.objects.get(pk=1)
    # userprofile = get_object_or_404(UserProfile, user=request.user)
    context = {'products':products,'pcategories':pcategories,'setting':setting}
    return render(request, 'home/about.html', context)

def searchresults(request):
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    setting = Setting.objects.get(pk=1)
    context = {'products':products,'pcategories':pcategories,'setting':setting}
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            lookUps = Q(title__icontains=query) | Q(price__icontains=query) | Q(description__icontains=query)
            object_list = Product.objects.filter(lookUps)
            context['object_list'] = object_list
            return render(request,'home/search_results.html', context)
        return render(request,'home/search_results.html', context)
    return render(request,'home/search_results.html', context)
    

class SearchResultsView(ListView):
    template_name = 'home/search_results.html'
    model = Product

    def get_queryset(self):
        setting = Setting.objects.get(pk=1)
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(price__icontains=query) | Q(description__icontains=query)
        )
        # context = {'setting':setting,'object_list':object_list}
        return object_list