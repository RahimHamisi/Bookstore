import pprint
import requests
from rest_framework.viewsets import ReadOnlyModelViewSet,ViewSet, ModelViewSet
from .models import Book,Collection, Genre
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer,CollectionSerializer, GenreSerializer, CollectionSerializers, CollectionSerializer1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.decorators import action


class BookViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class CollectionViewSet(ViewSet):
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_to_collection(self, request):
        book = get_object_or_404(Book,id=id)  
        print(book.id)
        serializer = CollectionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            collection = serializer.save() 
            print(collection)
            return Response({
                'message': 'Book added to collection successfully',
                'collection_name': collection.name,
                'book_title': book.title
            })
        return Response(serializer.errors, status=400)
    

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def view_collection(self, request):
        collections = Collection.objects.filter( user = request.user)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AddToCollectionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class=CollectionSerializer1

    #filter to get user's collections
    def get_queryset(self):
        user = self.request.user
        return Collection.objects.filter(user = user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        return serializer.data   