from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, generics, permissions
from rest_framework.parsers import MultiPartParser
from .models import WeddingRoomType, WeddingRoom, Employee, Customer, FoodCategory, ServiceCategory, Menu, Service, \
    WeddingBill, MenuAndCategory, CostsIncurred, WeddingRoomDeTails, User, Rating, BookTrip, Notification, MenuInBill, \
    ServiceInBill
from .serializers import WeddingRTSerializer, WeddingRoomSerializer, EmployeeSerializer, CustomerSerializer, \
    FoodCategorySerializer, ServiceCategorySerializer, MenuSerializer, ServiceSerializer, WeddingBillSerializer, \
    MenuAndCategorySerializer, CostsIncurredSerializer, WeddingRDetailsSerializer, UserSerializer, RatingSerializer, \
    BookTripSerializer, NotificationSerializer, MenuInBillSerializer, ServiceInBillSerializer

# Create your views here.


class WeddingRTViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingRoomType.objects.filter(active=True)
    serializer_class = WeddingRTSerializer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #
    #     return [permissions.IsAuthenticated()]


class WeddingRoomViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingRoom.objects.filter(active=True)
    serializer_class = WeddingRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Employee.objects.filter(active=True)
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Customer.objects.filter(active=True)
    serializer_class = CustomerSerializer


class FoodCategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = FoodCategory.objects.filter(active=True)
    serializer_class = FoodCategorySerializer


class ServiceCategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ServiceCategory.objects.filter(active=True)
    serializer_class = ServiceCategorySerializer


class MenuViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Menu.objects.filter(active=True)
    serializer_class = MenuSerializer


class ServiceViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceSerializer


class WeddingBillViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingBill.objects.all()
    serializer_class = WeddingBillSerializer


class MenuAndCategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = MenuAndCategory.objects.all()
    serializer_class = MenuAndCategorySerializer


class CostsIncurredViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = CostsIncurred.objects.all()
    serializer_class = CostsIncurredSerializer


class WeddingRDetailsViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingRoomDeTails.objects.all()
    serializer_class = WeddingRDetailsSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]


class RatingViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class BookTripViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset =BookTrip.objects.all()
    serializer_class = BookTripSerializer


class NotificationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class MenuInBillViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = MenuInBill.objects.all()
    serializer_class = MenuInBillSerializer


class ServiceInBillViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ServiceInBill.objects.all()
    serializer_class = ServiceInBillSerializer

def index(request):
    return HttpResponse("Quản Lý Nhà Hàng Tiệc Cưới")


# def welcome(request, year):
#     return HttpResponse("HELLO " + str(year))
#
#
# class TestView(View):
#     def get(self, request):
#         return HttpResponse("Testing")
#
#     def post(self,request):
#         pass