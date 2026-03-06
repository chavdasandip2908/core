
from django.contrib import admin
from django.urls import path
from home.views import *
from fuddy.views import ProductView
from fuddy.repositories import ProductRepository 
from account.views import RegisterView
from account.repositories import UserRepository

product_repo = ProductRepository()
user_repo = UserRepository()

product_view = ProductView(product_repo)  
user_view = RegisterView(user_repo)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('tutorial/', tutorial, name='tutorial'),
    path('users/', user_view.users_list, name='users'),
    path('update-product/<int:product_id>/', product_view.update_product, name='update_product'),
    path('delete-product/<int:product_id>/', product_view.delete_product, name='delete_product'),
    path('products/', product_view.products, name='products'),
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),
]
