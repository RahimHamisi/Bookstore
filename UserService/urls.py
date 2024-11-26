from django.urls import path # type: ignore
from django.urls.conf import include # type: ignore
from rest_framework import routers # type: ignore
from . import views

router=routers.DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns=router.urls

