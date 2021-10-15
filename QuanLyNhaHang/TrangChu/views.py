from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404
from .paginator import BasePagination
from .models import WeddingRoomType, WeddingRoom, Employee, Customer, FoodCategory, ServiceCategory, Menu, Service, \
    WeddingBill, CostsIncurred, WeddingRoomDeTails, User, Rating, Contact, Notification, MenuInBill, \
    ServiceInBill
from .serializers import WeddingRTSerializer, WeddingRoomSerializer, EmployeeSerializer, CustomerSerializer, \
    FoodCategorySerializer, ServiceCategorySerializer, MenuSerializer, ServiceSerializer, WeddingBillSerializer, \
    CostsIncurredSerializer, WeddingRDetailsSerializer, UserSerializer, RatingSerializer, \
    ContactSerializer, NotificationSerializer, MenuInBillSerializer, ServiceInBillSerializer, MenuDetailSerialize
from django.conf import settings
# Create your views here.
from django.db.models import Q

class WeddingRTViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingRoomType.objects.filter(active=True)
    serializer_class = WeddingRTSerializer
    pagination_class = BasePagination

    @action(methods=['get'], detail=True, url_path='weddingrooms')
    def get_weddingrooms(self, request, pk):
        weddingrooms = WeddingRoomType.objects.get(pk=pk).weddingrooms.filter(active=True)

        q = request.query_params.get('q')
        if q is not None:
            weddingrooms = weddingrooms.filter(Q(name__contains=q) | Q(description__contains=q) | Q(price__contains=q))

        return Response(WeddingRoomSerializer(weddingrooms, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #
    #     return [permissions.IsAuthenticated()]


class WeddingRoomViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = WeddingRoom.objects.filter(active=True)
    serializer_class = WeddingRoomSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        wedding_room = WeddingRoom.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            wedding_room = wedding_room.filter(Q(name__contains=q) | Q(description__contains=q) | Q(price__contains=q))

        wedding_room_category_id = self.request.query_params.get('wedding_room_category_id')
        if wedding_room_category_id is not None:
            wedding_room = wedding_room.filter(wedding_room_category_id=wedding_room_category_id)

        return wedding_room

    @action(methods=['get'], detail=True, url_path='weddingroombill')
    def get_weddingroombill(self, request, pk):
        weddingroombill = WeddingRoom.objects.get(pk=pk).weddingroombill.all()

        kw = request.query_params.get('kw')
        if kw is not None:
            weddingroombill = weddingroombill.filter(subject__icontains=kw)

        return Response(WeddingBillSerializer(weddingroombill, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


    @action(methods=['get'], detail=True, url_path='weddingroomdetails')
    def get_weddingroomdetails(self, request, pk):
        weddingroomdetails = WeddingRoom.objects.get(pk=pk).weddingroomdetails.all()

        kw = request.query_params.get('kw')
        if kw is not None:
            weddingroomdetails =  weddingroomdetails.filter(subject__icontains=kw)

        return Response(WeddingRDetailsSerializer( weddingroomdetails, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)
    # permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Employee.objects.filter(active=True)
    serializer_class = EmployeeSerializer
    pagination_class = BasePagination

    @action(methods=['get'], detail=True, url_path='employeebill')
    def get_employeebill(self, request, pk):
        employeebill = Employee.objects.get(pk=pk).employeebill.all()

        kw = request.query_params.get('kw')
        if kw is not None:
            employeebill = employeebill.filter(subject__icontains=kw)

        return Response(WeddingBillSerializer(employeebill, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Customer.objects.filter(active=True)
    serializer_class = CustomerSerializer
    pagination_class = BasePagination

    @action(methods=['get'], detail=True, url_path='customerbill')
    def get_customerbill(self, request, pk):
        customerbill = Customer.objects.get(pk=pk).customerbill.all()

        kw = request.query_params.get('kw')
        if kw is not None:
            customerbill = customerbill.filter(subject__icontains=kw)

        return Response(WeddingBillSerializer(customerbill, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


class FoodCategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = FoodCategory.objects.filter(active=True)
    serializer_class = FoodCategorySerializer
    pagination_class = BasePagination

    @action(methods=['get'], detail=True, url_path='menus')
    def get_menus(self, request, pk):
        menus = FoodCategory.objects.get(pk=pk).menus.filter(active=True)

        q = request.query_params.get('q')
        if q is not None:
            menus = menus.filter(Q(name__contains=q) | Q(description__contains=q) | Q(price__contains=q))

        return Response(MenuSerializer(menus, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


class ServiceCategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = ServiceCategory.objects.filter(active=True)
    serializer_class = ServiceCategorySerializer
    pagination_class = BasePagination

    @action(methods=['get'], detail=True, url_path='services')
    def get_services(self, request, pk):
        services = ServiceCategory.objects.get(pk=pk).services.filter(active=True)

        q = request.query_params.get('q')
        if q is not None:
            services = services.filter(Q(name__contains=q) | Q(description__contains=q) | Q(price__contains=q))

        return Response(ServiceSerializer(services, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


class MenuViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Menu.objects.filter(active=True)
    serializer_class = MenuSerializer
    # pagination_class = BasePagination

    def get_queryset(self):
        menus = Menu.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            menus = menus.filter(subject__icontains=q)

        foodcate_id = self.request.query_params.get('food_category')
        if foodcate_id is not None:
            menus = menus.filter(food_category=foodcate_id)

        return menus

    def get_queryset(self):
        menus = Menu.objects.filter(active=True)
        q = self.request.query_params.get('q')
        if q is not None:
            menus = menus.filter(Q(name__contains=q) | Q(description__contains=q) | Q(price__contains=q))
        foodcate_id = self.request.query_params.get('food_category')
        if foodcate_id is not None:
            menus = menus.filter(food_category=foodcate_id)
        return menus

    @action(methods=['get'], detail=True, url_path='menubills')
    def get_menubills(self, request, pk):
        menubills = Menu.objects.get(pk=pk).menubills.all()
        kw = request.query_params.get('kw')
        if kw is not None:
            menubills = menubills.filter(name__icontains=kw)

        return Response(MenuInBillSerializer(menubills, many=True,
                                       context={"request": request}).data,
                        status=status.HTTP_200_OK)



class ServiceViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        servies = Service.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            servies = servies.filter(Q(name__contains=q) | Q(description__contains=q) | Q(price__contains=q))

        service_category_id = self.request.query_params.get('service_category_id')
        if service_category_id is not None:
            servies = servies.filter(service_category_id=service_category_id)

        return servies

    @action(methods=['get'], detail=True, url_path='servicebills')
    def get_servicebills(self, request, pk):
        servicebills = Service.objects.get(pk=pk).servicebills.all()
        kw = request.query_params.get('kw')
        if kw is not None:
            servicebills = servicebills.filter(subject__icontains=kw)

        return Response(ServiceInBillSerializer(servicebills, many=True,
                                          context={"request": request}).data,
                        status=status.HTTP_200_OK)


class WeddingBillViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = WeddingBill.objects.all()
    serializer_class = WeddingBillSerializer
    pagination_class = BasePagination

    @action(methods=['get'], detail=True, url_path='weddingmenubills')
    def get_weddingmenubills(self, request, pk):
        weddingmenubills = WeddingBill.objects.get(pk=pk).weddingmenubills.all()

        kw = request.query_params.get('kw')
        if kw is not None:
            weddingmenubills = weddingmenubills.filter(subject__icontains=kw)

        return Response(MenuInBillSerializer(weddingmenubills, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)


    @action(methods=['get'], detail=True, url_path='weddingservicebills')
    def get_weddingservicebills(self, request, pk):
        weddingservicebills = WeddingBill.objects.get(pk=pk).weddingservicebills.all()

        kw = request.query_params.get('kw')
        if kw is not None:
            weddingservicebills = weddingservicebills.filter(subject__icontains=kw)

        return Response(ServiceInBillSerializer(weddingservicebills, many=True,
                                              context={"request": request}).data,
                        status=status.HTTP_200_OK)

#
# class MenuAndCategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset = MenuAndCategory.objects.all()
#     serializer_class = MenuAndCategorySerializer


class CostsIncurredViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = CostsIncurred.objects.all()
    serializer_class = CostsIncurredSerializer


class WeddingRDetailsViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingRoomDeTails.objects.all()
    serializer_class = WeddingRDetailsSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user, context={"request": request}).data,
                        status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ContactViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class NotificationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class MenuInBillViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = MenuInBill.objects.all()
    serializer_class = MenuInBillSerializer
    pagination_class = BasePagination


class ServiceInBillViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ServiceInBill.objects.all()
    serializer_class = ServiceInBillSerializer
    pagination_class = BasePagination


def index(request):
    return HttpResponse("Quản Lý Nhà Hàng Tiệc Cưới")


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)

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