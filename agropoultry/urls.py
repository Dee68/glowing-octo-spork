"""agropoultry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from home.views import aboutUs, contactUs
from account.views import RegistrationView,LoginView,logoutPage
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('/', include('home.urls', namespace='home')),
    path('products/', include('product.urls', namespace='products')),
    path('register/', RegistrationView.as_view(), name='register'),
    path('account/', include('account.urls', namespace='account')),
    # path('validate-username', csrf_exempt(UsernamevalidationView.as_view()), name='validate-username'),
    # path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutPage,name='logout'),
    path('about/', aboutUs, name='about'),
    path('contact/', contactUs, name='contact'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
