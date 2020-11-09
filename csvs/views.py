from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
# Importing the category model
from products.models import Category
# Importing the process that allows us to read the csv file
import csv
# from django.http import HttpResponse

# Create your views here.

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        # .csv reading process
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            # Loop process to read and skip the first row containg the titles
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    product = row[1].upper() 
                    # Category process
                    Category.objects.create(
                        product = product
                    )
                    # print(row)
                    # print(type(row))
            obj.activated = True
            obj.save()
    return render(request, 'csvs/upload.html', {'form': form})