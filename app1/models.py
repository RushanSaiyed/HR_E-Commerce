from datetime import date
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ManyToManyField(Category)
    Sub_Category = models.ManyToManyField(Sub_Category)
    name = models.CharField(max_length=90)
    price = models.IntegerField()
    des= models.TextField(default='')
    images= models.ImageField(upload_to='pro_img',blank=True,default='')

    
    def __str__(self):
        return self.name

        