from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# mutiple views can be created here and then imported in urls.py
# multiple line view
def home(request):
    return HttpResponse("""
    <h1>Welcome to the Home Page</h1>
    <p>This is the home page of our Django application.</p>
    """)
# one line view
def about(request):
    return HttpResponse("<h1>About Us</h1><p>This page provides information about our application.</p>")

# templeate view(html file)
def tutorial(request):
    return render(request, 'index.html')
# templeate view (specific folder vise )
def users(request):
    user_list = [
        {'name': 'Alice', 'email': 'alice@example.com','age': 15},
        {'name': 'Bob', 'email': 'bob@example.com','age': 25},
        {'name': 'Charlie', 'email': 'charlie@example.com','age': 35},
        {'name': 'David', 'email': 'david@example.com','age': 13},
        {'name': 'Eve', 'email': 'eve@example.com','age': 32}
    ]
    return render(request, 'users/user-listing.html', context={'users': user_list})