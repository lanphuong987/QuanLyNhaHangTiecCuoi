from .admin import admin_site
from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url


router = DefaultRouter()
router.register('User', views.UserViewSet)
router.register('WeddingRoomType', views.WeddingRTViewSet)
router.register('WeddingRoom', views.WeddingRoomViewSet)
router.register('WeddingRoomDetails', views.WeddingRDetailsViewSet)
router.register('Employee', views.EmployeeViewSet)
router.register('FoodCategory', views.FoodCategoryViewSet)
router.register('ServiceCategory', views.ServiceCategoryViewSet)
router.register('Menu', views.MenuViewSet)
router.register('Service', views.ServiceViewSet)
router.register('WeddingBill', views.WeddingBillViewSet)
router.register('Comments', views.CommentViewSet)
router.register('CostsIncurred', views.CostsIncurredViewSet)
router.register('Rating', views.RatingViewSet)
router.register('Contact', views.ContactViewSet)
router.register('Notification', views.NotificationViewSet)
router.register('MenuInBill', views.MenuInBillViewSet)
router.register('ServiceInBill', views.ServiceInBillViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    # path('welcome/<int:year>/', views.welcome, name="welcome"),
    # path('test/', views.TestView.as_view()),
    # re_path(r'welcome2/(?P<year>[0-9]{4})/$'),
    # path('admin/', admin_site.urls)
]
