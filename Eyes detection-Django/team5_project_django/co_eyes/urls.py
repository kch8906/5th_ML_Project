
from django.contrib import admin
from django.urls import path,include
from co_eyes import views

urlpatterns = [
    path('eyes/', views.co_eyes, name='co_eyes')
]
