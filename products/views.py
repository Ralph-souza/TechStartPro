#Importing processes from models.py, such as Product and Category
#Importing processes from models.py, such as ProductForm and DataForm   
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm

#Reading process 
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

#Creating process
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})

# #Updating process
# def update_product(request, id):
#     product = Product.objects.get(id=id)
#     form = ProductForm(request.POST or None, instance=product)

#     if form.is_valid():
#         form.save()
#         return redirect('list_products')

#     return render(request, 'products-form.html', {'form':form, 'product': product})

# #Deleting process
# def delete_product(request, id):
#     product = Product.objects.get(id=id)

#     if request.method == 'POST':
#         product.delete()
#         return redirect('list_products')

#     return render(request, 'prod-delete-confirm.html', {'product': product})

# Create your views here.
