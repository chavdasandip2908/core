from django.shortcuts import render, redirect


class ProductView:

    def __init__(self, repository):
        self.repo = repository

    def products(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            stock = request.POST.get('stock')

            success, message_or_product = self.repo.create(name, description, price, stock)

            if success:
                print(f"== Product '{name}' created successfully.")
            else:
                print(f"== {message_or_product}")

            return redirect('products')

        products = self.repo.get_all()

        if request.GET.get('search'):
            products = products.filter(name__icontains=request.GET.get('search'))

        return render(request, 'home.html', {'products': products , 'search': request.GET.get('search')})

    def update_product(self, request, product_id):
        product = self.repo.get_by_id(product_id)
        if not product:
            print("Product not found.")
            return redirect('products')

        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            stock = request.POST.get('stock')

            self.repo.update(product, name, description, price, stock)
            print(f"Product '{product.name}' updated successfully.")
            return redirect('products')

        return render(request, 'update_product.html', {'product': product})

    def delete_product(self, request, product_id):
        product = self.repo.get_by_id(product_id)
        if product:
            self.repo.delete(product)
            print(f"Product '{product.name}' deleted successfully.")
        else:
            print("Product not found.")
        return redirect('products')
