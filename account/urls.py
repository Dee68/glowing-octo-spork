from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name='account'

urlpatterns = [
  path('', views.index, name='userprofile'),
  path('validate-username', csrf_exempt(views.UsernamevalidationView.as_view()), name='validate-username'),
  path('validate-email', csrf_exempt(views.EmailValidation.as_view()), name='validate-email'),
  path('activate/<uid64>/<token>/', views.VerificationView.as_view(), name='activate'),
  # path('login/', views.loginPage, name='login'),
  # path('logout/', views.logoutPage,name='logout'),
]
