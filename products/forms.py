from django import forms
from .models import Product, Category

# form method for creating data
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'value']

# form method for creating categories
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

   