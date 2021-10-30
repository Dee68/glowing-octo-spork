from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import UserProfile
from product.models import Customer
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.mail import EmailMessage
from django.contrib import messages
from . utils import token_generator
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


import json
# Create your views here.
class RegistrationView(View):
    def get(self,request):
        context = {}
        return render(request, 'account/register.html', context)

    def post(self,request):
        username = request.POST['username']
        user_email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        context = {"fieldVals":request.POST}
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=user_email).exists():
                if len(password1) < 8:
                    messages.error(request,"password must be 8 characters or more")
                    return render(request, 'account/register.html', context)
                if not (password1 == password2):
                    messages.error(request, 'password did not match')
                    return render(request, 'account/register.html', context)
                    
                user = User.objects.create_user(username=username, email=user_email)
                user.set_password(password1)
                user.is_active=False
                user.save()
                current_user = request.user
                data = UserProfile()
                data1 = Customer()
                data1.user_id = current_user.id
                data.image = "uploads/profile_pics/userimage.png"
                data.save()
                data1.save()
                email_subject = 'Activate your account'
                # body of email should contain thr followings
                # -path to view
                # -get domain we are in
                # -get relative url
                
                # -get token

                # - encode uid
                uid64 = urlsafe_base64_encode(force_bytes(user.pk))

                # -get domain we are in
                domain = get_current_site(request).domain

                # -get relative url
                link = reverse('account:activate', kwargs={'uid64':uid64,'token':token_generator.make_token(user)})
                activate_link = 'http://'+domain+link

                email_body = 'Hello '+user.username+', please use the link below to verify your account\n'+activate_link
                email = EmailMessage(email_subject,email_body,'noreply@inuwaagropoultry.herokuapp.com',
                        [user_email,'ddimie283@gmail.com'] )

                email.send(fail_silently=False)
                messages.success(request,"Account successfully created")
                return render(request, 'account/register.html')           
        return render(request, 'account/register.html')


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
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        if User.objects.filter(email=email):
            return JsonResponse({'email_error':'Sorry,email already taken, choose another one'},status=409)
        return JsonResponse({'email_valid':True})

def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)