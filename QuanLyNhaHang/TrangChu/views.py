from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Quản Lý Nhà Hàng Tiệc Cưới")
