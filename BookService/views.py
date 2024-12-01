import pprint
import requests
from rest_framework.viewsets import ReadOnlyModelViewSet,ViewSet
from .models import Book,Collection
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer,CollectionSerializer
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
    def add_to_collection(self, request, pk):
        book = get_object_or_404(Book,id=pk)  
        serializer = CollectionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            collection = serializer.save() 
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
