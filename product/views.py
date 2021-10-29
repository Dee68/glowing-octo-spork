from django.shortcuts import render

# Create your views here.

# all products
def index(request):
    context = {}
    return render(request, 'product/index.html', context)