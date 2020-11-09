from django.shortcuts import render
from .models import Product

# Create your views here.

# Reading process od the CRUD
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})