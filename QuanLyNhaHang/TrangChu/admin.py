from django.contrib import admin
from django import forms
from .models import Employee, WeddingRoom, WeddingRoomType, WeddingRoomDeTails, Service, ServiceCategory, Customer
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class WeddingRForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = WeddingRoom
        fields = '__all__'


class WeddingRInline(admin.StackedInline):
    model = WeddingRoom
    pk_name = 'wedding_room_category'


class WeddingRTAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "description", "active"]
    inlines = (WeddingRInline, )


class WeddingRAdmin(admin.ModelAdmin):
    form = WeddingRForm
    list_display = ["name", "create_date", "price", "description", "active", "wedding_room_category"]


admin.site.register(Employee)
admin.site.register(Customer)

admin.site.register(WeddingRoomType, WeddingRTAdmin)
admin.site.register(WeddingRoom, WeddingRAdmin)
admin.site.register(WeddingRoomDeTails)

admin.site.register(Service)
admin.site.register(ServiceCategory)