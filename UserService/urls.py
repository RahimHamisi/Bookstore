from django.urls import path # type: ignore
from django.urls.conf import include # type: ignore
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from djoser.views import UserViewSet



urlpatterns=[
    path('login/',TokenObtainPairView.as_view()),
    path('register/',UserViewSet.as_view({'post': 'create'})),
    path('refresh-token/',TokenRefreshView.as_view())

]

