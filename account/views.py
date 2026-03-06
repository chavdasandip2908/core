from django.shortcuts import render, redirect

# Create your views here.

class RegisterView:
    def __init__(self, repository):
        self.repo = repository

    def register(self, request):
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

        return render(request, 'register.html')
    
    def login(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            success, message_or_user = self.repo.authenticate(email, password)

            if success:
                # Log in the user by storing user_id in session
                request.session['user_id'] = message_or_user.id
                print(f"== User '{message_or_user.name}' logged in successfully.")
                return redirect('users')
            else:
                print(f"== {message_or_user}")

            return redirect('login')

        return render(request, 'login.html')

    def logout(self, request):
        # Clear the session
        if 'user_id' in request.session:
            del request.session['user_id']
        return redirect('login')

    def users_list(self, request):
        # Check if user is authorized (simple session check)
        if 'user_id' not in request.session:
            print("== Unauthorized access attempt to users list.")
            return redirect('login')

        users = self.repo.get_all_users()
        print(users[0].created_at)
        return render(request, 'users.html', {'users': users})

