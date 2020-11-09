from django.urls import path
from .views import list_products, create_products, update_product, delete_product

app_name = 'products'

urlpatterns = [
    path('', list_products, name="list_products"),
    path('new', create_products, name="create_products"),
    path('update/<int:id>/', update_product, name="upgrade_product"),
    path('delete/<int:id>/', delete_product, name="delete_product"),
]