from django import forms
from .models import Product

# Product form parameters
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'value', 'category']
