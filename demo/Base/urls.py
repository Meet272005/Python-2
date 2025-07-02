from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from Base import views

urlpatterns = [
    path("",views.home),
    path("room/",views.room)
]
