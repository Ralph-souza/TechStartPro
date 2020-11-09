from django.db import models

# Create your models here.

#This class will permit to upload de .csv files
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f" File id: {self.id}"