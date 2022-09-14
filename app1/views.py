from itertools import product
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from app1.models import Category, Product


# Create your views here.
def login_page(request):
    return render(request, 'accounts/login.html')


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home/home.html', {'cate':category, 'pro':products})