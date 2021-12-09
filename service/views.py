from django.shortcuts import render,get_object_or_404
from home.models import Setting
from account.models import UserProfile
from product.models import *
from .models import Service
# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    # userprofile = get_object_or_404(UserProfile, user=request.user)
    pictures = Picture.objects.filter(title__contains='slider')
    # pcat = get_object_or_404(Category, slug=category_slug)
    pcategories = Category.objects.filter(parent=None)
    services = Service.objects.all()
    # categories = Category.objects.filter(parent=pcat)
    ctx = {'setting':setting,'pcategories':pcategories,'pictures':pictures,
    'services':services}
    return render(request,'services/index.html',ctx)

def service_detail(request, slug):
    setting = Setting.objects.get(pk=1)
    # userprofile = get_object_or_404(UserProfile, user=request.user)
    pictures = Picture.objects.filter(title__contains='slider')
    pcategories = Category.objects.filter(parent=None)
    service = get_object_or_404(Service, slug=slug)
    return render(request,'services/service_detail.html',{'service':service,'pcategories':pcategories,
    'pictures':pictures,'setting':setting})