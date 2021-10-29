from django.urls import path
from .import views

app_name='products'

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:id>/<str:slug>/',views.product_details, name='product_details'),

    ]