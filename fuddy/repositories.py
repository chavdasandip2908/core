from .models import Product
from django.db import IntegrityError

class ProductRepository:
    @staticmethod
    def get_all():
        return Product.objects.all()

    @staticmethod
    def get_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def get_by_name(name):
        try:
            return Product.objects.filter(name=name)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def create(name, description, price, stock):
        if Product.objects.filter(name=name).exists():
            return False, f"Product with name '{name}' already exists."
        
        try:
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                stock=stock
            )
            return True, product
        except IntegrityError:
            return False, "Integrity error occurred."

    @staticmethod
    def update(product, name, description, price, stock):
        product.name = name
        product.description = description
        product.price = price
        product.stock = stock
        product.save()
        return product

    @staticmethod
    def delete(product):
        product.delete()
        return True
