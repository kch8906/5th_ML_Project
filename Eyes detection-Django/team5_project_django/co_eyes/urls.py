from django.contrib import admin
from django.urls import path
from co_eyes import views

app_name = 'co_eyes'
urlpatterns = [
    path('eyes/', views.predict, name='eyes')
]