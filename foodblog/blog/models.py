from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Auto Created User Table

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If user is deleted, post also deleted

    #Object won't be returned, we get sensible data returned
    def __str__(self):
        return self.title

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_cost = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='images/', default="no image")

    def __str__(self):
        return self.product_name
# Create your models here.
