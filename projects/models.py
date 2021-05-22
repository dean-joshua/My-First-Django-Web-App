from django.db import models
from django.conf import settings
import os

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtlink = models.URLField(max_length=200, default="")
    gittlink = models.URLField(max_length=200, default="")
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.title
