from django.db import models

# How to run the migration:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

# how manage the data from shell
# 1. python manage.py shell => to open the shell
# CRUD operations
# Create:
# 1. - car = User(name='John Doe', email='john@example.com', password='secret')
#    - car.save()
# 2. User.objects.create(name='John Doe', email='john@example.com', password='secret')
# Read:
# 1. User.objects.all() => to get all users
# 2. User.objects.filter(name='John Doe') => to get users with name 'john doe'
# 3. User.objects.get(id=1) => to get user with id 1
# Update:
# 1. - user = User.objects.get(id=1)
#    - user.name = 'Jane Doe'
#    - user.save()
# 2. User.objects.filter(id=1).update(name='Jane Doe')
# Delete:
# 1. - user = User.objects.get(id=1)
#    - user.delete()
# 2. User.objects.filter(id=1).delete()

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField( blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    stock = models.IntegerField(default=0)


