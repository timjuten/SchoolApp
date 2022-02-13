from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_users, name="all-users"),
    path('create', create_user, name='create-user')
]