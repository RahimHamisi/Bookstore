from django.urls import path,include
from rest_framework import routers

from BookService.views import BookViewSet,CollectionViewSet


router=routers.DefaultRouter()
router.register('books',BookViewSet,basename='books')

collection_viewset = CollectionViewSet.as_view({
    'post': 'add_to_collection',
    'get': 'view_collection'
})
urlpatterns=[
    path("",include(router.urls)),
    path('collections/add_to_collection/', collection_viewset, name='add_to_collection'),
    path('collections/view_collection/', collection_viewset, name='view_collection'),

   
]