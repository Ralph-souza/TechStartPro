from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.description

class Category(models.Model):
    name = models.CharField(max_length=50)

# Create your models here.