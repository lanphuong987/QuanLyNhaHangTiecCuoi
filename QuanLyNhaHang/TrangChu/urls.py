from django.contrib import admin
from django.urls import path, include, re_path
from. import views

urlpatterns = [
    path('', views.index, name='Home'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
