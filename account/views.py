from django.shortcuts import render
from django.views import View
# Create your views here.
class RegistrationView(View):
    def get(self,request):
        context = {}
        return render(request, 'account/register.html', context)




def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)