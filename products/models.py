from django.db import models

# Create your models here.

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