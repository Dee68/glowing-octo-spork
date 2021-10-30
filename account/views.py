from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.validators import validate_email
import json
# Create your views here.
class RegistrationView(View):
    def get(self,request):
        context = {}
        return render(request, 'account/register.html', context)


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