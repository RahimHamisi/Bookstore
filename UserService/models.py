from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username=models.CharField(max_length=200,unique=True)
    email=models.EmailField(blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile_pictures',blank=True)
    bio=models.TextField()
    address=models.TextField(null=True,blank=True)
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    preference=models.ManyToManyField("BookService.Genre",blank=True,null=True)


    def __str__(self) -> str:
        return f"THe profile for {self.user.username}"
