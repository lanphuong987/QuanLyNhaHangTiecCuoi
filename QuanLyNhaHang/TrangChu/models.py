from collections import deque


# import abstract as abstract
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m')
    phone = models.CharField(max_length=15, null=True, unique=True)
    address = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    id_card = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='User_Employee')
    position = models.IntegerField(null=False)
    address = models.TextField(null=True, blank=True)
    type = models.IntegerField(null=False)
    date_start = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


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
    description = RichTextField(null=True)

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
    wedding_room_category = models.ForeignKey(WeddingRoomType, on_delete=models.CASCADE, related_name='weddingrooms')


class Menu(Base):
    hinh = models.ImageField(upload_to='menu/%Y/%m')
    food_category = models.ForeignKey(FoodCategory, null=True, on_delete=models.SET_NULL, related_name= 'menus')


# class MenuAndCategory(models.Model):
#     menu_category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, related_name='MenuCategory' )
#     menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, related_name='MenuId')


class Service(Base):
    hinh = models.ImageField(upload_to='service/%Y/%m')
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')


class WeddingRoomDeTails(models.Model):
    shift = models.IntegerField(null=False)
    price = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    wedding_room = models.ForeignKey(WeddingRoom, on_delete=models.CASCADE, related_name='weddingroomdetails')

    def __str__(self):
        return self.wedding_room.name


class WeddingBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='customerbill')
    create_date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField()
    guest = models.IntegerField(null=False)
    total = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    earnest_money = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    is_organize = models.BooleanField(default=False)
    pay_off = models.BooleanField(default=False)
    wedding_room = models.ForeignKey(WeddingRoom, on_delete=models.CASCADE, related_name='weddingroombill')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='employeebill')

    def __str__(self):
        return self.user.name


class CostsIncurred(models.Model):
    price = models.DecimalField(null=False, max_digits= 15, decimal_places=2)
    reason = models.TextField(null=True, blank=False)
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='Incurred')


class ActionBase (models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='billrating')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='userrating')

    class Meta:
        abstract = True


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.creator.username


class Comment(models.Model):
    content = models.TextField()
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='billcomment')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomment')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='UserNotification')
    notification = models.TextField(null=False, blank=False)
    is_read = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.TextField(null=True, blank=False)
    is_confirmed = models.BooleanField(default=False)
    phone = models.TextField(null=True, blank=False)
    email = models.TextField(null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    address = models.TextField(null=True, blank=False)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='EmployeeBook')


class MenuInBill(models.Model):
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='weddingmenubills')
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, related_name='menubills')
    price = models.DecimalField(null=False, max_digits=15, decimal_places=2)


class ServiceInBill(models.Model):
    wedding_bill = models.ForeignKey(WeddingBill, on_delete=models.CASCADE, related_name='weddingservicebills')
    service = models.ForeignKey(Menu,on_delete=models.SET_NULL, null=True, related_name='servicebills')
    price = models.DecimalField(null=False, max_digits=15, decimal_places=2)