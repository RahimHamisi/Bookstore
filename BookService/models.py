from django.db import models
import UserService
from django.conf import settings
import uuid
# Create your models here.


class Genre(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Science', 'Science'),
        ('Fantasy', 'Fantasy'),
        ('Biography', 'Biography'),
        ('Romance', 'Romance'),
        ('Children', 'Children'),
    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200,choices=GENRE_CHOICES)


class Book(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description=models.TextField(blank=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    genre=models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True)


    def __str__(self) :
        return self.title


class Collection(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    book=models.ManyToManyField(Book,related_name='book')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="collection")

    def __str__(self) :
        return self.name
   

