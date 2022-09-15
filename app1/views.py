from email import message
import imp
from itertools import product
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from app1.models import Category, Member, Product



# Create your views here.

def home(request):
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    
    if categoryID:
        products = Product.objects.filter(Sub_Category = categoryID)
    else:
        products = Product.objects.all()

    return render(request, 'home/home.html', {'cate':category, 'pro':products})


def login(request):
        if request.method == 'POST':
            try:
                email = request.POST['email']
                password = request.POST['password']

                credentials = Member.objects.get(email=email)
                if credentials.password == password:
                    return redirect('home')
                else:
                    messages.info(request, 'Wrong Password')
            except:
                messages.info(request, 'Wrong Email')
        return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        obj = Member()
        obj.username = request.POST['username']
        obj.email = request.POST['email']
        obj.phone = request.POST['phone']
        obj.password = request.POST['password']
        print(obj.password)
        obj.confirm_password = request.POST['confirm_password']
        print(obj.confirm_password)

        if obj.confirm_password == obj.password:
            obj.save()
            messages.success(
                request, 'Your account have been successfully created')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')
    return render(request, 'account/signup.html')