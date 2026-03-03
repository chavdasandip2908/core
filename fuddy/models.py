from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField( blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    stock = models.IntegerField(default=0)
