from django.db import models

# How to run the migration:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField( blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    stock = models.IntegerField(default=0)


