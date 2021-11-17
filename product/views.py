from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from home.models import Setting
from django.conf import settings
from .forms import ShippingForm
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.

# all products
def index(request):
    setting = Setting.objects.get(pk=1)
    pictures = Picture.objects.filter(title__contains='slider')
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    products = Product.objects.all()
    context = {'products':products,'pictures':pictures,'pcategories':pcategories,'setting':setting}
    return render(request, 'products/index.html', context)

# detail of  a single product
def product_details(request, id, slug):
    setting = Setting.objects.get(pk=1)
    pictures = Picture.objects.filter(title__contains='slider')
    product = get_object_or_404(Product,id=id, slug=slug)
    pcategories = Category.objects.filter(parent=None)
    ppictures = Picture.objects.filter(product=product)
    context = {'product':product,'pcategories':pcategories,
    'ppictures':ppictures,'pictures':pictures,'setting':setting}
    return render(request, 'products/product_details.html', context)

# get parent subcategories
def show_category(request, category_slug):
    setting = Setting.objects.get(pk=1)
    pictures = Picture.objects.filter(title__contains='slider')
    pcat = get_object_or_404(Category, slug=category_slug)
    pcategories = Category.objects.filter(parent=None)
    categories = Category.objects.filter(parent=pcat)
    context = {'pcategories':pcategories, 'categories':categories,
    'pictures':pictures,'setting':setting}
    return render(request, 'products/show_category.html', context)

# gets products of a given category ****
def category_products(request, cslug=None):
    setting = Setting.objects.get(pk=1)
    pictures = Picture.objects.filter(title__contains='slider')
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    pcategories = Category.objects.filter(parent=None)
    if cslug:
        category = get_object_or_404(Category, slug=cslug)
        products = products.filter(category=category)
    
    context = {'products':products,
    'categories':categories,'category':category,'pcategories':pcategories,
    'pictures':pictures,'setting':setting}
    
    return render(request, 'products/category_product.html', context)

# show cart details
@login_required(login_url='/login')# check for login
def add_to_cart(request):
    context = {}
    pcategories = Category.objects.filter(parent=None)
    setting = Setting.objects.get(pk=1)
    context['pcategories']= pcategories
    context['setting'] = setting
    
    if request.user.is_authenticated:
        items = Cart.objects.filter(customer__id=request.user.id, status=False)
        context['items'] = items
        if request.method == "POST":
            pid = request.POST['pid']
            qty = request.POST['qty']
            do_exist = Cart.objects.filter(product__id=pid, customer__id=request.user.id, status=False)
            if len(do_exist) > 0:
                messages.warning(request,'Item already exists in your cart.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            else:
                product = get_object_or_404(Product, id=pid)
                usr = get_object_or_404(User,id=request.user.id)
                c = Cart(customer=usr, product=product,quantity=qty)
                c.save()
                messages.success(request, '{}  Added to your cart'.format(product.title))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    else:
        # Anonymouse user
        pass
    pcategories = Category.objects.filter(parent=None)
    context['pcategories']= pcategories
    return render(request, 'products/cart_detail.html', context)

#using ajax to get cart details
def get_cart_data(request):
    items = Cart.objects.filter(customer__id=request.user.id, status=False)
    # set initial values to 0
    total,quantity,num = 0,0,0
    #loop through items in cart
    for item in items:
        total += float(item.product.price) * item.quantity# cart total
        quantity += int(item.quantity)
        num += 1# number of items in cart
    res = {"total":total,"quantity":quantity,'"num':num}
    return JsonResponse(res)
        

        
    
    
    

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(Cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(Cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)

# process payment using paypal
@login_required(login_url='/login')# check for login
def process_payment(request):
    items = Cart.objects.filter(customer_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.product.title)+"\n"
        p_ids += str(j.product.id)+","
        amt += float(j.product.price)
        inv +=  str(j.id)
        cart_ids += str(j.id)+","
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(customer=usr,cart_id=cart_ids,product_ids=p_ids,invoice_id=inv)
    ord.save()
    ord.transaction_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'products/process_payment.html', {'form': form})

# show checkout page
@login_required(login_url='/login')# check for login
def checkout(request):
    setting = Setting.objects.get(pk=1)
    items = Cart.objects.filter(customer__id=request.user.id, status=False)
    usr = User.objects.get(username=request.user.username)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.product.title)+"\n"
        p_ids += str(j.product.id)+","
        amt += float(j.product.price)
        inv +=  str(j.id)
        cart_ids += str(j.id)+","
    ord = Order(customer=usr,cart_id=cart_ids,product_ids=p_ids,invoice_id=inv)
    customer = request.user
    form = ShippingForm()
    print(customer)
    #print(request.user)
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        fieldVal = request.POST
        pcategories = Category.objects.filter(parent=None)
        if form.is_valid():
            data = ShippingAddress(order=ord)#initialize object
            data.customer = customer
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.zipcode = form.cleaned_data['zipcode']
            ord.save()
            data.save()
            context = {'pcategories':pcategories,'items':items,'form':form,'setting':setting,'customer':customer}
            render(request, 'products/checkout.html', context)
            messages.success(request,'Shipping info successfully created.')
            return HttpResponseRedirect(request. META['HTTP_REFERER'])
        else:
            messages.error(request,'Please fill in the required fields, to proceed further.')
            return HttpResponseRedirect(request. META['HTTP_REFERER'])
    pcategories = Category.objects.filter(parent=None)
    context={'pcategories':pcategories,'items':items,'form':form,'setting':setting,'customer':customer}
    return render(request, 'products/checkout.html', context)

@login_required(login_url='/login')# check for login
def payment_done(request):
    return HttpResponse("Payment Successful.")

@login_required(login_url='/login')# check for login
def payment_cancelled(request):
    return HttpResponse("Payment Cancelled.")

