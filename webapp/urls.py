from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('signup', views.signup),
    path('userlogin', views.userlogin, name="login"),
    path('update', views.update),
    path('logout', views.signout),
    path('profile', views.profile),
    path('upload', views.upload),

]