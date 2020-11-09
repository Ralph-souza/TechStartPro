# Generated by Django 2.2.17 on 2020-11-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.CharField(choices=[('MOVEIS', 'moveis'), ('DECORACAO', 'decoracao'), ('CELULAR', 'celular'), ('INFORMATICA', 'informatica'), ('BRINQUEDOS', 'brinquedos')], max_length=50)),
            ],
        ),
    ]
