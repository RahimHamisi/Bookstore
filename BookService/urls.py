from django.urls import path,include
from rest_framework import routers

from BookService.views import BookViewSet,CollectionViewSet


router=routers.DefaultRouter()
router.register('books',BookViewSet,basename='books')
router.register('collections',CollectionViewSet,basename='collection')
urlpatterns=[
    path("",include(router.urls)),

   
]