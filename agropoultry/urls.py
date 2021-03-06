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
from home.views import aboutUs, contactUs, SearchResultsView,searchresults
from product.views import process_payment, payment_done, payment_cancelled
from account.views import RegistrationView,LoginView,logoutPage
from django.contrib.auth import views as auth_views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('products/', include('product.urls', namespace='products')),
    path('services/', include('service.urls', namespace='services')),
    path('register/', RegistrationView.as_view(), name='register'),
    path('account/', include('account.urls', namespace='account')),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/', searchresults, name='search_results'),
    # path('validate-username', csrf_exempt(UsernamevalidationView.as_view()), name='validate-username'),
    # path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutPage,name='logout'),
    path('about/', aboutUs, name='about'),
    path('contact/', contactUs, name='contact'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process_payment/', process_payment, name='process_payment'),
    path('payment_done/', payment_done, name='payment_done'),
    path('payment_cancelled/', payment_cancelled, name='payment_cancelled'),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # authentication views from django
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), 
    name='password_reset'),
    path('reset_password/done/', 
    auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'), 
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'), 
    name='password_reset_confirm'),
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), 
    name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
