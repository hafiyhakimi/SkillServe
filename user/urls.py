from django.urls import path
from django.urls import re_path as url, include
from . import views
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'user'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    # Define other URL patterns here
]

urlpatterns += staticfiles_urlpatterns()