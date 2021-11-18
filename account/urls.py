from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name='account'

urlpatterns = [
  path('', views.index, name='userprofile'),
  path('validate-username', csrf_exempt(views.UsernamevalidationView.as_view()), name='validate-username'),
  path('validate-email', csrf_exempt(views.EmailValidation.as_view()), name='validate-email'),
  path('activate/<uid64>/<token>/', views.VerificationView.as_view(), name='activate'),
  path('update/', views.profile_update, name='update'),
  path('change_password/', views.update_password, name='change_password'),
  path('whishlist/', views.whishlist,name='whishlist'),
  path('add_to_wishlist/<int:id>/', views.add_to_whishlist, name='add_to_wishlist'),
]
