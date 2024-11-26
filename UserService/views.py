from django.http import HttpResponse # type: ignore
from rest_framework.mixins import CreateModelMixin,  RetrieveModelMixin, UpdateModelMixin # type: ignore
from rest_framework.viewsets import GenericViewSet # type: ignore

from .serializers import UserCreateSerializer

from .models import User


# Create your views here.



# class UserViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class=UserCreateSerializer