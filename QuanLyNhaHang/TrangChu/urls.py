from .admin import admin_site
from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('WeddingRoomType', views.WeddingRTViewSet)
router.register('WeddingRoom', views.WeddingRoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('welcome/<int:year>/', views.welcome, name="welcome"),
    # path('test/', views.TestView.as_view()),
    # re_path(r'welcome2/(?P<year>[0-9]{4})/$'),
    # path('admin/', admin_site.urls)
]
