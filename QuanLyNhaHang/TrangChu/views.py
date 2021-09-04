from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions
from .models import WeddingRoomType, WeddingRoom
from .serializers import WeddingRTSerializer, WeddingRoomSerializer

# Create your views here.


class WeddingRTViewSet(viewsets.ModelViewSet):
    queryset = WeddingRoomType.objects.filter(active=True)
    serializer_class = WeddingRTSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class WeddingRoomViewSet(viewsets.ModelViewSet):
    queryset = WeddingRoom.objects.filter(active=True)
    serializer_class = WeddingRoomSerializer

def index(request):
    return HttpResponse("Quản Lý Nhà Hàng Tiệc Cưới")


def welcome(request, year):
    return HttpResponse("HELLO " + str(year))


class TestView(View):
    def get(self, request):
        return HttpResponse("Testing")

    def post(self,request):
        pass