
from django.contrib import admin
from django.urls import path
from home.views import *
from fuddy.views import ProductView
from fuddy.repositories import ProductRepository

repo = ProductRepository()
product_view = ProductView(repo)  

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('tutorial/', tutorial, name='tutorial'),
    path('users/', users, name='users'),
    path('update-product/<int:product_id>/', product_view.update_product, name='update_product'),
    path('delete-product/<int:product_id>/', product_view.delete_product, name='delete_product'),
    path('products/', product_view.products, name='products'),
    path('admin/', admin.site.urls),
]
