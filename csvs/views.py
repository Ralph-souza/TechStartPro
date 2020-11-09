from django.shortcuts import render
from .forms import CsvModelForm
# from django.http import HttpResponse

# Create your views here.

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    return render(request, 'csvs/upload.html', {'form': form})