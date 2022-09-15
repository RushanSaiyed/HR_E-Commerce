from django.contrib import admin
from .models import Category, Member, Sub_Category, Product
from django.contrib.auth.models import Group,User


# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Member)
