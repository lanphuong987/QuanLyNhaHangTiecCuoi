from rest_framework.serializers import ModelSerializer
from .models import WeddingRoomType, WeddingRoom, Employee, Customer, FoodCategory, ServiceCategory, Menu, Service, \
    WeddingBill, MenuAndCategory, CostsIncurred, Rating, Notification, BookTrip, MenuInBill, WeddingRoomDeTails, \
    ServiceInBill, User


class WeddingRTSerializer(ModelSerializer):
    class Meta:
        model = WeddingRoomType
        fields = ["id", "name", "create_date", "description"]


class WeddingRoomSerializer(ModelSerializer):
    # wedding_room_category = WeddingRTSerializer()
    class Meta:
        model = WeddingRoom
        fields = ["id", "name", "price", "create_date", "hinh_chinh_dien", "max" ]


class WeddingRDetailsSerializer(ModelSerializer):
    wedding_room = WeddingRoomSerializer()
    class Meta:
        model = WeddingRoomDeTails
        fields = ["shift", "price", "wedding_room"]


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["position", "address", "type", "date_start"]


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["fullname", "phonecus", "email", "address", "date_start"]


class FoodCategorySerializer(ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ["name", "create_date", "description", "active"]


class ServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["name", "create_date", "description", "active"]


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ["name", "hinh", "price", "description", "create_date", "active"]


class ServiceSerializer(ModelSerializer):
    service_category = ServiceCategorySerializer()
    class Meta:
        model = Service
        fields = ["name", "hinh", "price", "description", "create_date", "active", "service_category"]


class WeddingBillSerializer(ModelSerializer):
    customer = CustomerSerializer()
    employee = EmployeeSerializer()
    wedding_room = WeddingRoomSerializer()
    class Meta:
        model = WeddingBill
        fields = ["employee", "customer", "create_date", "date_start", "guest", "total", "earnest_money",
                  "is_organize", "pay_off", "wedding_room"]


class MenuAndCategorySerializer(ModelSerializer):
    menu_category = FoodCategorySerializer()
    menu = MenuSerializer()
    class Meta:
        model = MenuAndCategory
        fields = ["menu_category", "menu"]


class CostsIncurredSerializer(ModelSerializer):
    wedding_bill = WeddingBillSerializer()
    class Meta:
        model = CostsIncurred
        fields = ["price", "reason", "wedding_bill"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "phone", "avatar"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class RatingSerializer(ModelSerializer):
    wedding_bill = WeddingBillSerializer()
    user = UserSerializer()
    class Meta:
        model = Rating
        fields = ["user", "create_date", "comment", "is_contact", "wedding_bill"]


class NotificationSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Notification
        fields = ["user", "notification", "is_read"]


class BookTripSerializer(ModelSerializer):
    user = UserSerializer()
    employee = EmployeeSerializer()
    class Meta:
        model = BookTrip
        fields = ["user", "employee", "time", "is_confirmed"]


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