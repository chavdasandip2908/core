from .models import User
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
class UserRepository:
    def create(self, name, email, password):
        try:
            # first check user exits
            user = User.objects.filter(email=email).first()
            if user:
                return False, "Email already exists."
            # hash password
            user = User.objects.create(name=name, email=email, password=make_password(password))
            return True, user
        except IntegrityError:
            return False, "Unexpected error occurred."
    
    def authenticate(self, email, password):
        try:
            user = User.objects.filter(email=email).first()
            # user exists and compare hash password
            if user and check_password(password, user.password):
                return True, user
            return False, "Invalid credentials."
        except IntegrityError:
            return False, "Unexpected error occurred."

    def get_all_users(self):
        users = User.objects.all()
        return [user for user in users if user.password]

    def get_user_by_id(self, user_id):
        user = User.objects.filter(id=user_id).first()
        if user:
            return user
        return False, "User not found."

    def update_user(self, user_id, name, email, password):
        try:
            user = self.get_user_by_id(user_id)
            if user:
                user.name = name
                user.email = email
                user.password = make_password(password)
                user.save()
            return True, user
        except IntegrityError:
            return False, "Unexpected error occurred."

    def delete_user(self, user_id):
        try:
            user = self.get_user_by_id(user_id)
            if user:
                user.delete()
                return True, "User deleted successfully."
            return False, "User not found."
        except IntegrityError:
            return False, "Unexpected error occurred."