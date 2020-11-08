# Generated by Django 2.2.17 on 2020-11-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeingDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]