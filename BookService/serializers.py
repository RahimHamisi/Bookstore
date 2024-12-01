from rest_framework import serializers
from BookService.models import Book,Collection, Genre
from django.conf import settings

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['id','name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','description','publication_date','price','publisher','is_active']

class CollectionSerializer(serializers.ModelSerializer):
    genre=GenreSerializer()
    book=BookSerializer(many=True)
    user=settings.AUTH_USER_MODEL
    
    class Meta:
        model=Collection
        fields=['id','name','genre','book','user']
        extra_kwargs = {
            'user': {'read_only': True}  
        }
    def validate(self, data):
            user = self.context['request'].user
            collection = Collection.objects.filter(user=user, name=data['collection_name']).first()
            if not collection:
                raise serializers.ValidationError("Collection with this name doesn't exist.")
            data['collection'] = collection
            return data

    def save(self):
        book = Book.objects.get(id=self.validated_data['book_id'])
        collection = self.validated_data['collection']
        collection.book.add(book)  
        return collection