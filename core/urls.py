from django.contrib import admin
from django.urls import path, include
from home.views import *
from fuddy.views import ProductView
from fuddy.repositories import ProductRepository 
from account.views import RegisterView
from account.repositories import UserRepository

product_repo = ProductRepository()
user_repo = UserRepository()

product_view = ProductView(product_repo)  

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('tutorial/', tutorial, name='tutorial'),
    path('update-product/<int:product_id>/', product_view.update_product, name='update_product'),
    path('delete-product/<int:product_id>/', product_view.delete_product, name='delete_product'),
    path('products/', product_view.products, name='products'),
    path('admin/', admin.site.urls),
    
    # Reusable Auth App
    path('account/', include('account.urls')),
    # SSO / Allauth paths
    path('accounts/', include('allauth.urls')),
]
