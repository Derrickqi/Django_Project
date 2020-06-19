from django.urls import path, re_path , include
from . import views

urlpatterns = [
    path('user-list/', views.register),
]