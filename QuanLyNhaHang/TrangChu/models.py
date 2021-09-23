from collections import deque


# import abstract as abstract
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m')
    phone = models.CharField(max_length=10, null=True, unique=True)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='User_Employee')
    position = models.IntegerField(null=False)
    address = models.TextField(null=True, blank=True)
    type = models.IntegerField(null=False)
    date_start = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='User_Customer')
    fullname = models.TextField(null=True, blank=True)
    phonecus = models.CharField(max_length=10, null=True, unique=True)
    email = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CategoryBase(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=100, null=False, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Base(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=150, null=False)
    price = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


class WeddingRoomType(CategoryBase):
    description = models.TextField(null=True, blank=True)


class FoodCategory(CategoryBase):
    description = models.TextField(null=True, blank=True)


class ServiceCategory(CategoryBase):
    description = models.TextField(null=True, blank=True)


class WeddingRoom(Base):
    hinh_chinh_dien = models.ImageField(upload_to='sanhcuoi/%Y/%m')
    max = models.IntegerField(null=False)
    wedding_room_category = models.ForeignKey(WeddingRoomType, on_delete=models.CASCADE, related_name='WeddingRoomType')


class Menu(Base):
    hinh = models.ImageField(upload_to='menu/%Y/%m')


class MenuAndCategory(models.Model):
    menu_category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, related_name='MenuCategory' )
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, related_name='MenuId')


class Service(Base):
    hinh = models.ImageField(upload_to='service/%Y/%m')
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='ServiceCategory')


class WeddingRoomDeTails(models.Model):
    shift = models.IntegerField(null=False)
    price = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    wedding_room = models.ForeignKey(WeddingRoom, on_delete=models.CASCADE, related_name='WeddingRopmDetails')


class WeddingBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='CustomerBill')
    create_date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField()
    guest = models.IntegerField(null=False)
    total = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    earnest_money = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    is_organize = models.BooleanField(default=False)
    pay_off = models.BooleanField(default=False)
    wedding_room = models.ForeignKey(WeddingRoom, on_delete=models.CASCADE, related_name='WeddingRoomBill')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='EmployeeBill')


class CostsIncurred(models.Model):
    price = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    reason = models.TextField(null=True, blank=False)
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='Incurred')


class Rating(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='BillRating')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='UserRating')
    comment = models.TextField(null=True, blank=False)
    is_contact = models.BooleanField(default=False)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='UserNotification')
    notification = models.TextField(null=False, blank=False)
    is_read = models.BooleanField(default=False)


class BookTrip(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    is_confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserBook')
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='EmployeeBook')


class MenuInBill(models.Model):
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='MIBBill')
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, related_name='MIBMenu')
    price = models.DecimalField(null=False, max_digits=15, decimal_places=2)


class ServiceInBill(models.Model):
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='SIBBill')
    service = models.ForeignKey(Menu,on_delete=models.SET_NULL, null=True, related_name='SIBService')
    price = models.DecimalField(null=False, max_digits=15, decimal_places=2)