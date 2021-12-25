import datetime

from django.contrib import admin
from django.contrib.auth.models import Permission
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from django.http import JsonResponse


from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

# Form CKEditor

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


class WeddingRForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = WeddingRoom
        fields = '__all__'


# WeddingRoom Admin

class WeddingRInline(admin.StackedInline):
    model = WeddingRoom
    pk_name = 'wedding_room_category'
    # readonly_fields = ["image"]

    # def image(self, weddingroom):
    #     return mark_safe(
    #         " <img src = '/static/{img_url}' width='120px'/>".format(img_url=weddingroom.hinh_chinh_dien.name))


class WeddingRTAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "active"]
    list_filter = ["name", "active"]
    inlines = (WeddingRInline, )


class WeddingRAdmin(admin.ModelAdmin):
    form = WeddingRForm
    list_display = ["name", "create_date", "price", "active", "wedding_room_category"]
    list_filter = ["name"]
    readonly_fields = ["image"]

    def image(self, weddingroom):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=weddingroom.hinh_chinh_dien.name))


class WeddingRDetailAdmin(admin.ModelAdmin):
    list_display = ["shift", "price", "wedding_room"]
    list_filter = ["price"]


# User Admin

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
    search_fields = ["first_name", "last_name", "email", "phone"]
    list_filter = ["first_name", "last_name"]
    readonly_fields = ["image"]

    def image(self, user):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=user.avatar.name))


# Employee Admin

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "position", "type", "date_start", "active"]
    search_fields = ["user__username"]



# Bill Admin

class MenuBillInlineAdmin(admin.StackedInline):
    model = MenuInBill
    fk_name = 'wedding_bill'


class ServiceBillInlineAdmin(admin.StackedInline):
    model = ServiceInBill
    fk_name = 'wedding_bill'


class WeddingBillAdmin (admin.ModelAdmin):
    list_display = ["id", "user", "date_start", "wedding_room", "total"]
    inlines = [MenuBillInlineAdmin, ServiceBillInlineAdmin, ]
    search_fields = ["user__username", "wedding_room__name"]
    list_filter = ["user", "date_start"]
    ordering = ("-date_start",)


# Service Admin

class ServiceInline(admin.StackedInline):
    model = Service
    pk_name = 'service_category'
    # readonly_fields = ["image"]

    # def image(self, service):
    #     return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=service.hinh.name))


class ServiceCateAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "active"]
    search_fields = ["name"]
    inlines = (ServiceInline, )


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ["name", "create_date", "price", "active", "service_category"]
    search_fields = ["name", "price"]
    list_filter = ["name", "price"]
    readonly_fields = ["image"]

    def image(self, service):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=service.hinh.name))


# Menu Admin

class MenuInline(admin.StackedInline):
    model = Menu
    pk_name = 'food_category'
    # readonly_fields = ["image"]

    # def image(self, menu):
    #     return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=menu.hinh.name))


class FoodCateAdmin(admin.ModelAdmin):
    list_display = ["name", "create_date", "active"]
    search_fields = ["name", "create_date"]
    list_filter = ["name"]
    inlines = (MenuInline, )


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ["name", "create_date", "price", "active", "food_category"]
    search_fields = ["name", "price"]
    list_filter = ["name", "price"]
    readonly_fields = ["image"]

    def image(self, menu):
        return mark_safe(" <img src = '/static/{img_url}' width='120px'/>".format(img_url=menu.hinh.name))


# Ratting & Comment Admin

class RatingAdmin(admin.ModelAdmin):
    list_display = ["creator", "rate", "wedding_bill", "created_date", "updated_date"]
    search_fields = ["user__username"]
    list_filter = ["creator", "rate"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["creator", "content", "wedding_bill", "created_date", "updated_date"]
    search_fields = ["user__username"]
    list_filter = ["creator", "content"]


# Report Chart Admin

class ReportAdmin(admin.ModelAdmin):
    def year_chart(self, request):
        labels = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9',
                  'Tháng 10', 'Tháng 11', 'Tháng 12']
        Jan = 0
        Feb = 0
        Mar = 0
        Apr = 0
        May = 0
        Jun = 0
        Jul = 0
        Aug = 0
        Sep = 0
        Oct = 0
        Nov = 0
        Dec = 0

        if request.method == 'POST':
            getYear = request.form.get('thang')
            count = WeddingBill.objects.all()
            for temp in count:
                year = datetime.datetime.strptime(temp['date_start'], "%Y/%m/%d %H:%M:%S").year
                if year == getYear:
                    month = datetime.datetime.strptime(temp['date_star'], "%Y/%m/%d %H:%M:%S").month

                if month == 1:
                    Jan += temp['total']
                elif month == 2:
                    Feb += temp['total']
                elif month == 3:
                    Mar += temp['total']
                elif month == 4:
                    Apr += temp['total']
                elif month == 5:
                    May += temp['total']
                elif month == 6:
                    Jun += temp['total']
                elif month == 7:
                    Jul += temp['total']
                elif month == 8:
                    Aug += temp['total']
                elif month == 9:
                    Sep += temp['total']
                elif month == 10:
                    Oct += temp['total']
                elif month == 11:
                    Nov += temp['total']
                else:
                    Dec += temp['total']

        data = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

        return JsonResponse(data={
            'labels': labels,
            'data': data,
        })

    def month_chart(self, request):
        get_month = request.form.get('thang')
        get_year = request.form.get('nam')
        turnover = 0
        count = WeddingBill.objects.all()
        for temp in count:
            year = datetime.datetime.strptime(temp['date_start'], "%Y/%m/%d %H:%M:%S").year
            month = datetime.datetime.strptime(temp['date_start'], "%Y/%m/%d %H:%M:%S").month
            if year == get_year and month == get_month:
                turnover += temp['total']

        return turnover


# Admin Site

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


admin_site = QLNHAppAdminSite('Nhà Hàng Tiệc Cưới')


admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.site.register(WeddingRoomType, WeddingRTAdmin)
admin.site.register(WeddingRoom, WeddingRAdmin)
admin.site.register(WeddingRoomDeTails, WeddingRDetailAdmin)
admin.site.register(WeddingBill, WeddingBillAdmin)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCateAdmin)

admin.site.register(FoodCategory, FoodCateAdmin)
admin.site.register(Menu, MenuAdmin)

admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Contact)
admin.site.register(Notification)
admin.site.register(CostsIncurred)

admin.site.register(Permission)
