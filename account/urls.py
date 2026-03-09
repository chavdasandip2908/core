from django.urls import path
from .views import RegisterView
from .repositories import UserRepository

user_repo = UserRepository()
account_view = RegisterView(user_repo) 

urlpatterns = [
    path('forget-password/', account_view.forget_password, name='forget_password'), 
    path('set-password/', account_view.set_password, name='set_password'), 
    path('register/', account_view.register, name='register'), 
    path('login/', account_view.login_view, name='login'), 
    path('logout/', account_view.logout_view, name='logout'), 
    path('users/', account_view.users_list, name='users'), 
]
