from django.urls import path,include
from rest_framework import routers

from BookService import views


router=routers.DefaultRouter()
router.register(r'books',views.BookViewSet,basename='books')
urlpatterns=[
    path("",include(router.urls)),

   
]