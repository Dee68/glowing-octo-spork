from django.urls import path
from .import views

app_name='products'

urlpatterns = [
    path('', views.index, name='products'),
    path('cart/', views.add_to_cart, name='cart_details'),
    path('get_cart_data/', views.get_cart_data, name='get_cart_data'),
    path("change_quan",views.change_quan,name="change_quan"),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:id>/<str:slug>/',views.product_details, name='product_details'),
    path('category/<str:category_slug>/', views.show_category, name='show_category'),
    path('<str:cslug>/', views.category_products, name='category_products'), 

    ]