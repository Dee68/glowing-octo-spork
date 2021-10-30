from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
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
            return JsonResponse({'username_error':'Username should contain only alphanumeric characters.'}, status=400, safe=False)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry username already in use, choose another.'}, status=409, safe=False)
        else:
            return JsonResponse({'username_valid':True}, status=200, safe=False)

def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)