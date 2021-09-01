from .admin import admin_site
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('admin/', admin_site.urls)
]
