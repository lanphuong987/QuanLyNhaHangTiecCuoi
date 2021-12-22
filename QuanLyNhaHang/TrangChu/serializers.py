from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class WeddingRTSerializer(ModelSerializer):
    class Meta:
        model = WeddingRoomType
        fields = ["id", "name", "create_date", "description"]


class WeddingRoomSerializer(ModelSerializer):
    # wedding_room_category = WeddingRTSerializer()
    hinh_chinh_dien = SerializerMethodField()

    def get_hinh_chinh_dien(self, WeddingRoom):
        request = self.context['request']
        name = WeddingRoom.hinh_chinh_dien.name
        if name.startswith("static/"):
            path = '/%s' %name
        else:
            path = '/static/%s' %name
        return request.build_absolute_uri(path)

    class Meta:
        model = WeddingRoom
        fields = ["id", "name", "price", "create_date", "hinh_chinh_dien", "max", "wedding_room_category_id", "description"]


class WeddingRDetailsSerializer(ModelSerializer):
    wedding_room = WeddingRoomSerializer()
    class Meta:
        model = WeddingRoomDeTails
        fields = ["shift", "price", "wedding_room"]


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "position", "address", "type", "date_start"]


class FoodCategorySerializer(ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ["id", "name", "create_date", "description", "active"]


class ServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "name", "create_date", "description", "active"]


class MenuSerializer(ModelSerializer):
    hinh = SerializerMethodField()

    def get_hinh(self, Menu):
        request = self.context['request']
        name = Menu.hinh.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        return request.build_absolute_uri(path)

    class Meta:
        model = Menu
        fields = ["id", "name", "hinh", "price", "description", "create_date", "active"]


class MenuDetailSerialize(MenuSerializer):
    class Meta:
        model = MenuSerializer.Meta.model
        fields = MenuSerializer.Meta.fields + ['food_category']


class ServiceSerializer(ModelSerializer):
    hinh = SerializerMethodField()

    def get_hinh(self, Service):
        request = self.context['request']
        name = Service.hinh.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        return request.build_absolute_uri(path)

    service_category = ServiceCategorySerializer()
    class Meta:
        model = Service
        fields = ["name", "hinh", "price", "description", "create_date", "active", "service_category","id"]



# class MenuAndCategorySerializer(ModelSerializer):
#     menu_category = FoodCategorySerializer()
#     menu = MenuSerializer()
#     class Meta:
#         model = MenuAndCategory
#         fields = ["menu_category", "menu"]



class UserSerializer(ModelSerializer):
    # avatar = SerializerMethodField()
    #
    # def get_avatar(self, User):
    #     request = self.context['request']
    #     name = User.avatar.name
    #     if name.startswith("static/"):
    #         path = '/%s' % name
    #     else:
    #         path = '/static/%s' % name
    #     return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "phone", "avatar", "date_joined", "is_superuser", "about", "address"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)

    # def save(self, **kwargs):
    #     if self.instance.avatar:
    #         self.instance.avatar.delete()
    #     return super().save()


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate", "created_date"]


class WeddingBillSerializer(ModelSerializer):
    # employee = EmployeeSerializer()
    menus = MenuSerializer(many=True)
    services = ServiceSerializer(many=True)
    wedding_room = WeddingRoomSerializer()

    def get_user(self, rating):
        return UserSerializer(rating.user, context={"request": self.context.get('request')}).data

    class Meta:
        model = WeddingBill
        fields = ["id", "create_date", "date_start", "guest", "total", "earnest_money",
                  "is_organize", "pay_off", "wedding_room", "user", "menus", "services"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_date", "updated_date"]


class NotificationSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Notification
        fields = ["user", "notification", "is_read"]


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "employee_id", "phone", "is_confirmed", "email", "content","address"]


class MenuInBillSerializer(ModelSerializer):
    wedding_bill = WeddingBillSerializer()
    menu = MenuSerializer()
    class Meta:
        model = MenuInBill
        fields = ["wedding_bill", "menu", "price"]


class ServiceInBillSerializer(ModelSerializer):
    wedding_bill = WeddingBillSerializer()
    service = MenuSerializer()
    class Meta:
        model = ServiceInBill
        fields = ["wedding_bill", "service", "price"]


class CostsIncurredSerializer(ModelSerializer):
    wedding_bill = WeddingBillSerializer()

    class Meta:
        model = CostsIncurred
        fields = ["price", "reason", "wedding_bill"]