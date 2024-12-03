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

    def save(self):
        book = Book.objects.get(id=self.validated_data['book_id'])
        collection = self.validated_data['collection']
        collection.book.add(book)  
        return collection


#use this when you want to create a new collection with a new book and a new genre
class CollectionSerializers(serializers.ModelSerializer):
    genre=GenreSerializer()
    book=BookSerializer(many = True)
    user=settings.AUTH_USER_MODEL
    
    class Meta:
        model=Collection
        fields=['id','name','genre','book','user']
        extra_kwargs = {
            'user': {'read_only': True}  
        }
        
    #due to that genre and book are not in the database we need to tell django to create them
    def create(self, validated_data):
        genre = validated_data.pop("genre")
        books = validated_data.pop("book")
        created_books = []
        for book in books:
            print(book.items())
            created_book = Book.objects.create(**book)
            created_books.append(created_book)

        found= Genre.objects.create(**genre)

        data = Collection.objects.create(genre = found, **validated_data)

        #for many to many 
        data.book.set(created_books)
        return data
    

#this is for creating a new collection with an existing book and an existing genre
class CollectionSerializer1(serializers.ModelSerializer):
    user=settings.AUTH_USER_MODEL
    class Meta:
        model =Collection
        fields=['id','name','genre','book','user']
        extra_kwargs = {
            'user': {'read_only': True}  
        }