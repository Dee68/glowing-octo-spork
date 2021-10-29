from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

# all products
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product/index.html', context)

def product_details(request, id, slug):
   
    pictures = Picture.objects.filter(title__contains='slider')
    product = get_object_or_404(Product,id=id, slug=slug)
    pcategories = Category.objects.filter(parent=None)
    ppictures = Picture.objects.filter(product=product)
    context = {'product':product,'pcategories':pcategories,
    'ppictures':ppictures,'pictures':pictures}
    return render(request, 'products/product_details.html',context)