from rest_framework.serializers import ModelSerializer
from .models import WeddingRoomType, WeddingRoom


class WeddingRTSerializer(ModelSerializer):
    class Meta:
        model = WeddingRoomType
        fields = ["id", "name", "create_date", "description"]


class WeddingRoomSerializer(ModelSerializer):
    wedding_room_category = WeddingRTSerializer()
    class Meta:
        model = WeddingRoom
        fields = ["id", "name", "price", "create_date", "max", "wedding_room_category" ]