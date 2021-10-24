from django.contrib import admin
from django.contrib.auth.models import Permission
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe

from .models import Employee, WeddingRoom, WeddingRoomType, WeddingRoomDeTails, Service, ServiceCategory, User, Comment
from .models import FoodCategory, Menu, MenuInBill, WeddingBill, CostsIncurred, Rating, Notification, Contact, ServiceInBill
from .serializers import UserSerializer
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
# Register your models here.


class WeddingRForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = WeddingRoom
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Service
        fields = '__all__'


class MenuForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Menu
        fields = '__all__'


class WeddingRInline(admin.StackedInline):
    model = WeddingRoom
    pk_name = 'wedding_room_category'
    readonly_fields = ["image"]

    def image(self, weddingroom):
        return mark_safe(
            " <img src = '/static/{img_url}' width='120px'/>".format(img_url=weddingroom.hinh_chinh_dien.name))


class WeddingRTAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "description", "active"]
    inlines = (WeddingRInline, )


class WeddingRAdmin(admin.ModelAdmin):
    form = WeddingRForm
    list_display = ["name", "create_date", "price", "description", "active", "wedding_room_category"]
    readonly_fields = ["image"]

    def image(self, weddingroom):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=weddingroom.hinh_chinh_dien.name))


class UserCreationForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ["username", "first_name", "last_name", "email", "phone", "date_joined", "is_active"]
    readonly_fields = ["image"]

    def image(self, user):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=user.avatar.name))


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "position", "type", "date_start", "active"]


class WeddingRDetailAdmin(admin.ModelAdmin):
    list_display = ["shift", "price", "wedding_room"]


class WeddingBillAdmin (admin.ModelAdmin):
    list_display = ["user", "date_start", "wedding_room", "total", "employee"]


class MenuBillAdmin(admin.ModelAdmin):
    list_display = ["wedding_bill", "menu", "price"]


class ServiceBillAdmin(admin.ModelAdmin):
    list_display = ["wedding_bill", "service", "price"]


class ServiceInline(admin.StackedInline):
    model = Service
    pk_name = 'service_category'
    readonly_fields = ["image"]

    def image(self, service):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=service.hinh.name))


class ServiceCateAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "description", "active"]
    inlines = (ServiceInline, )


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ["name", "create_date", "price", "description", "active", "service_category"]
    readonly_fields = ["image"]

    def image(self, service):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=service.hinh.name))


class MenuInline(admin.StackedInline):
    model = Menu
    pk_name = 'food_category'
    readonly_fields = ["image"]

    def image(self, menu):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=menu.hinh.name))


class FoodCateAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "description", "active"]
    inlines = (MenuInline, )


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ["name", "create_date", "price", "description", "active", "food_category"]
    readonly_fields = ["image"]

    def image(self, menu):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=menu.hinh.name))


class RatingAdmin(admin.ModelAdmin):
    list_display = ["creator", "rate", "wedding_bill", "created_date", "updated_date"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["creator", "content", "wedding_bill", "created_date", "updated_date"]


class QLNHAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY NHA HANG TIEC CUOI'

    def get_urls(self):
        return [
            path('qlnh-stats/', self.qlnh_stats)
        ] + super().get_urls()

    def qlnh_stats(self, request):
        weddingroomtype_count = WeddingRoomType.objects.count()
        stats = WeddingRoomType.objects.annotate(weddingroom_count=Count('WeddingRoomype')).values("id", "name", "weddingroom_count")

        return TemplateResponse(request, 'admin/qlnh-stats.html', {
            'weddingroomtype_count': weddingroomtype_count,
            'stats': stats
        })


admin_site = QLNHAppAdminSite('NHTC')

# admin_site.register(Employee)
# admin_site.register(Customer)
#
# admin_site.register(WeddingRoomType, WeddingRTAdmin)
# admin_site.register(WeddingRoom, WeddingRAdmin)
# admin_site.register(WeddingRoomDeTails)
#
# admin_site.register(Service)
# admin_site.register(ServiceCategory)
admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.site.register(WeddingRoomType, WeddingRTAdmin)
admin.site.register(WeddingRoom, WeddingRAdmin)
admin.site.register(WeddingRoomDeTails, WeddingRDetailAdmin)
admin.site.register(WeddingBill, WeddingBillAdmin)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCateAdmin)
admin.site.register(ServiceInBill, ServiceBillAdmin)

admin.site.register(FoodCategory, FoodCateAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuInBill, MenuBillAdmin)

admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact)
admin.site.register(Notification)
admin.site.register(CostsIncurred)

admin.site.register(Permission)