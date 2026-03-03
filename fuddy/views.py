from django.shortcuts import render,redirect    
from .models import *

# Create your views here.

from django.contrib import messages
from django.db import IntegrityError


def products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        if Product.objects.filter(name=name).exists():
            print(f"== Product with name '{name}' already exists.")
        else:
            try:
                Product.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    stock=stock,
                )
                print(f"== Product '{name}' created successfully.")
            except IntegrityError:
                print(f"== Unable to save product '{name}' due to integrity constraints.")

        # redirect after POST to prevent duplicate submissions
        return redirect('products')

    # Get all products from the database
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if request.method == 'POST':
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.price = request.POST.get('price')
            product.stock = request.POST.get('stock')
            product.save()
            print(f"Product '{product.name}' updated successfully.")
            return redirect('products')
        return render(request, 'update_product.html', {'product': product})
    except Product.DoesNotExist:
        print("Product not found.")
        return redirect('products')

def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        print(f"Product '{product.name}' deleted successfully.")
    except Product.DoesNotExist:
        print("Product not found.")
    return redirect('products')