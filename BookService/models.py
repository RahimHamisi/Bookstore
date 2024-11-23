from django.db import models
import UserService
from UserService.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    genre=models.ForeignKey("Genre",on_delete=models.SET_NULL,null=True)


    def __str__(self) :
        return self.title

class Genre(models.Model):
    name=models.CharField(max_length=200)

class Collection(models.Model):
    name=models.CharField(max_length=200)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    book=models.ManyToManyField(Book)
    user=models.ForeignKey("UserService.User",on_delete=models.CASCADE,related_name="collection")

    def __str__(self) :
        return self.name
   

