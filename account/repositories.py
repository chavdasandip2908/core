from .models import User, PasswordResetCode
from django.db import IntegrityError
from django.contrib.auth import authenticate
import random
from django.core.mail import send_mail

class UserRepository:
    def create(self, name, email, password):
        try:
            if User.objects.filter(email=email).exists():
                return False, "Email already exists."
            username = email.split('@')[0]
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            return True, user
        except IntegrityError:
            return False, "Unexpected error occurred."
    
    def authenticate_user(self, email, password):
        user = authenticate(email=email, password=password)
        if user is not None:
            return True, user
        return False, "Invalid credentials."

    def get_all_users(self):
        return User.objects.all()

    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def generate_reset_code(self, email):
        user = User.objects.filter(email=email).first()
        if not user:
            return False, "User with this email does not exist."
        
        # Generate 6 digit code
        code = str(random.randint(100000, 999999))
        PasswordResetCode.objects.filter(email=email).delete() # Remove old codes
        PasswordResetCode.objects.create(email=email, code=code)
        
        # Send Email (handled by console backend in settings)
        send_mail(
            'Your Password Reset Code',
            f'Your 6-digit reset code is: {code}',
            'noreply@fuddy.com',
            [email],
            fail_silently=False,
        )
        return True, "Code sent successfully."

    def verify_reset_code(self, email, code, new_password):
        reset_entry = PasswordResetCode.objects.filter(email=email, code=code).first()
        
        if not reset_entry:
            return False, "Invalid reset code."
        
        if not reset_entry.is_valid():
            return False, "Code has expired. Please request a new one."
        
        user = User.objects.filter(email=email).first()
        if user:
            user.set_password(new_password)
            user.save()
            reset_entry.delete() # Cleanup
            return True, "Password reset successfully."
        return False, "User not found."
