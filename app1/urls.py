from django.urls import path

from .views import login_page, home

urlpatterns = [
   path('', home, name="home"),
   path('login/', login_page, name="login")
]