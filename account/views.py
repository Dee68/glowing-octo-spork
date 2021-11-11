from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from product.models import Customer,Product,Category
from django.http import JsonResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import EmailMessage
from django.contrib import messages
from . utils import token_generator
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.safestring import mark_safe
from .forms import RegisterUserForm,UserProfileForm, UserUpdateForm, ChangePasswordForm
from home.models import Setting


import json
# Create your views here.
class RegistrationView(View):
    def get(self,request):
        return render(request, 'account/register.html')

    def post(self,request):
        form = RegisterUserForm()
        context = {'form':form}
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            fieldVals = request.POST
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            user_email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            context = {"fieldVals":fieldVals, 'form':form}
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already in use, choose another one.")
                return render(request, 'account/register.html', context)
            if User.objects.filter(email=user_email).exists():
                messages.error(request, "sorry email already in use, please choose another one.")
                return render(request, 'account/register.html', context)
            if len(password1) < 8:
                messages.error(request,"password must be 8 characters or more")
                return render(request, 'account/register.html', context)
            if not (password1 == password2):
                messages.error(request, 'passwords did not match')
                return render(request, 'account/register.html', context)        
                    
            if (len(firstname) == 0 or len(lastname) == 0):
                messages.error(request, mark_safe("Please fill in all fields,<br> they are all required"))
                return render(request, 'account/register.html', context)
            if form.is_valid():
                user = User.objects.create_user(username=username, email=user_email, 
                password=password1,first_name=firstname,last_name=lastname)
                user.set_password(password1)
                # form.save()
                user.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                current_user = request.user
                data = UserProfile()
                #data1 = Customer()
                        
                data.user_id = current_user.id
                #data1.user_id = current_user.id
                data.image = "uploads/profile_pics/userimage.png"
                data.save()
                #data1.save()
                messages.success(request,mark_safe("Account created successfully.<br>You can now log in."))
                return render(request, 'account/register.html', context)
            else:
                messages.error(request, "Invalid form, please fill in all fields.")  
                return render(request, 'account/register.html', context)

                        
                    # messages.error(request, "Invalid form, please fill in all fields.")  
                    # return render(request, 'account/register.html', context)
        return render(request, 'account/register.html', context)
        
                
                    
                
                
            
        
        
                    
                
                #user.is_active=False
                
                #email_subject = 'Activate your account'
                # body of email should contain the followings
                # -path to view
                # -get domain we are in
                # -get relative url
                
                # -get token

                # - encode uid
                #uid64 = urlsafe_base64_encode(force_bytes(user.pk))

                # -get domain we are in
                #domain = get_current_site(request).domain

                # -get relative url
                #link = reverse('account:activate', kwargs={'uid64':uid64,'token':token_generator.make_token(user)})
                #activate_link = 'http://'+domain+link

                #email_body = 'Hello '+user.username+', please use the link below to verify your account\n'+activate_link
                #email = EmailMessage(email_subject,email_body,'noreply@inuwaagropoultry.com',[user_email] )

                #email.send(fail_silently=False)
                # messages.success(request,"Account successfully created")
                # return render(request, 'account/register.html')           
            #return render(request, 'account/register.html')
        

# path to view from email
class VerificationView(View):
    def get(self,request,uid64,token):
        try:
            id = force_text(urlsafe_base64_decode(uid64))
            user = User.objects.get(pk=id)
            if not token_generator.check_token(user, token):
                messages.warning(request, 'user alredy activated')
                return redirect('login')
            if user.is_active:
                return redirect('account:login')
            user.is_active = True
            user.save()
            messages.success(request,'Account successfully activated')
            return redirect('login')
        except Exception as ex:
            pass
        return redirect('login')



class UsernamevalidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should contain only alphanumeric characters.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry username already in use, choose another.'}, status=409)
        
        return JsonResponse({'username_valid':True}, status=200)

class EmailValidation(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        if User.objects.filter(email=email):
            return JsonResponse({'email_error':'Sorry,email already taken, choose another one'},status=409)
        try:
            validate_email(email)
            return JsonResponse({'email_valid':True}, status=200)
        except ValidationError:
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        # if not validate_email(email):
        #     return JsonResponse({'email_error':'Email is invalid'},status=400)
        # if User.objects.filter(email=email):
        #     return JsonResponse({'email_error':'Sorry,email already taken, choose another one'},status=409)
        #return JsonResponse({'email_valid':True})

class LoginView(View):
    def get(self,request):
        return render(request, 'account/login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    messages.success(request, 'Welcome, '+user.username)
                    return redirect('home:home')
                messages.info(request, 'Account not activated, please check your email')
                return render(request, 'account/login.html')
            
            messages.error(request,'Invalid credentials, try again')
            return render(request, 'account/login.html')

        messages.error(request, 'Please fill all fields to login')
        return render(request, 'account/login.html')

# profile update page
@login_required(login_url='/login')# check for login
def profile_update(request):
    setting = Setting.objects.get(pk=1)
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('/account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    context = {'user_form':user_form,'profile_form':profile_form,'products':products,
    'pcategories':pcategories,'userprofile':userprofile,'setting':setting }
    return render(request, 'account/update_profile.html', context)

@login_required(login_url='/login')# check for login
def update_password(request):
    setting = Setting.objects.get(pk=1)
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Password successfully changed.')
            return HttpResponseRedirect("/account")
        else:
            messages.error(request, str(form.errors))
            return HttpResponseRedirect("/account/change_password")
    form = ChangePasswordForm(request.user)    
    
    context = {'form':form,'products':products,'pcategories':pcategories,
    'userprofile':userprofile,'setting':setting}
    return render(request, 'account/update_password.html', context)
            

# def loginPage(request):
#     context = {}
#     return render(request, 'account/login.html', context)

# profile page
@login_required(login_url='/login')# check for login
def index(request):
    setting = Setting.objects.get(pk=1)
    products = Product.objects.all()
    pcategories = Category.objects.filter(parent=None)
    current_user = request.user
    userprofile = UserProfile.objects.get(user_id=current_user.id)
    context = {'userprofile':userprofile,'products':products,
    'pcategories':pcategories,'setting':setting}
    return render(request, 'account/index.html', context)

# logout
def logoutPage(request):
    logout(request)
    return redirect('/')