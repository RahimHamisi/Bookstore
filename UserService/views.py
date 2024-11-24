from django.http import HttpResponse
from rest_framework.mixins import CreateModelMixin,  RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import UserProfileSerializer

from .models import UserProfile


# Create your views here.



class ProfileViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class=UserProfileSerializer