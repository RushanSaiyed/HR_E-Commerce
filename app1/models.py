from dataclasses import fields
from datetime import date
from distutils.command.upload import upload
from email.policy import default
from genericpath import exists
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

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


class Member(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(default='')
    phone = models.IntegerField(default='')
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.email



# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='Email', error_messages={'exists':'Email Already Exists'})

#     class Meta:
#       model = User
#       fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
        
#         if commit:
#             user.save()
#         return user

#     def clean_email(self):
#         if User.objects.filter(email=self.cleaned_data['email']).exists():
#             raise forms.ValidationError(self.fields['email'])
#         return self.cleaned_data['email']
        