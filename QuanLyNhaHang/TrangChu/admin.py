from django.contrib import admin
from .models import Employee, WeddingRoom, WeddingRoomType, WeddingRoomDeTails, Service, ServiceCategory

# Register your models here.


class WeddingRTAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "description", "active"]

admin.site.register(Employee)

admin.site.register(WeddingRoomType, WeddingRTAdmin)
admin.site.register(WeddingRoom)
admin.site.register(WeddingRoomDeTails)

admin.site.register(Service)
admin.site.register(ServiceCategory)