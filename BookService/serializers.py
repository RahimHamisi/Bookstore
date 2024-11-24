from rest_framework import serializers

from BookService.models import Book,Collection, Genre

class GenreSerializer(serializers.Serializer):
    class Meta:
        model=Genre
        fields=['id','name']


class BookSerializer(serializers.Serializer):
    genre=GenreSerializer()


    class Meta:
        model=Book
        fields=['id','title','author','genre','description','publication_date','price','publisher','is_active']

class CollectionSerializer(serializers.Serializer):
    genre=GenreSerializer()
    book=BookSerializer()
    
    class Meta:
        model=Collection
        fields=['id','name','genre','book','user']