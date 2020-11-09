from django.db import models

# Create your models here.

# Products Data Base
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category

# Categories Data Base
CATEGORY_CHOICES = (
    ('MOVEIS', 'moveis'),
    ('DECORACAO', 'decoracao'),
    ('CELULAR', 'celular'),
    ('INFORMATICA', 'informatica'),
    ('BRINQUEDOS', 'brinquedos')
)

class Category(models.Model):
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.category}"