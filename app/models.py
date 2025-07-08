from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='images/')
    Description=models.TextField()
    Author=models.CharField(max_length=100)
    Created_on=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.Title

