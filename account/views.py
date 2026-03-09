from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class RegisterView:
    def __init__(self, repository):
        self.repo = repository

    def register(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            success, message_or_user = self.repo.create(name, email, password)

            if success:
                print(f"== User '{name}' created successfully.")
                return redirect('login')
            else:
                print(f"== {message_or_user}")

            return redirect('register')

        return render(request, 'account/register.html')
    
    def login_view(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            success, message_or_user = self.repo.authenticate_user(email, password)

            if success:
                login(request, message_or_user)
                print(f"== User '{message_or_user.get_full_name() or message_or_user.username}' logged in successfully.")
                return redirect('home')
            else:
                print(f"== {message_or_user}")

            return redirect('login')
        
        reset_status = request.GET.get('reset')
        message = None
        if reset_status == 'success':
            message = "Password reset successfully. You can now login."
            
        return render(request, 'account/login.html', {'title': 'Login', 'success_message': message})

    def logout_view(self, request):
        auth_logout(request)
        return redirect('login')

    def users_list(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        users = self.repo.get_all_users()
        return render(request, 'account/users.html', {'users': users})

    def forget_password(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        
        if request.method == 'POST':
            email = request.POST.get('email')
            success, message = self.repo.generate_reset_code(email)
            if success:
                return render(request, 'account/password_reset.html', {'success': message, 'email': email})
            return render(request, 'account/password_reset.html', {'error': message})
            
        return render(request, 'account/password_reset.html')

    def set_password(self, request):
        if request.user.is_authenticated:
            return redirect('home')
            
        if request.method == 'POST':
            email = request.POST.get('email')
            code = request.POST.get('code')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if password != confirm_password:
                return render(request, 'account/set_password.html', {'error': "Passwords do not match.", 'email': email, 'code': code})
            
            success, message = self.repo.verify_reset_code(email, code, password)
            if success:
                return redirect(f"{reverse('login')}?reset=success")
            return render(request, 'account/set_password.html', {'error': message, 'email': email, 'code': code})

        email = request.GET.get('email', '')
        return render(request, 'account/set_password.html', {'email': email})
