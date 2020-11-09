from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

# Reading process of the CRUD
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

# Creating process of the CRUD
def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/products-form.html', {'form': form}) 