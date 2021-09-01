from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse

from .models import Employee, WeddingRoom, WeddingRoomType, WeddingRoomDeTails, Service, ServiceCategory, Customer
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
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

admin_site.register(Employee)
admin_site.register(Customer)

admin_site.register(WeddingRoomType, WeddingRTAdmin)
admin_site.register(WeddingRoom, WeddingRAdmin)
admin_site.register(WeddingRoomDeTails)

admin_site.register(Service)
admin_site.register(ServiceCategory)