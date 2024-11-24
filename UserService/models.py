from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username=models.CharField(max_length=200,unique=True)
    email=models.EmailField(blank=True,unique=True)
    date_joined=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile_pictures',blank=True)
    bio=models.TextField(blank=True)
    address=models.TextField(null=True,blank=True)
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    birth_date=models.DateField(blank=True,null=True)
   


    def __str__(self) -> str:
        return f"THe profile for {self.user.username}"
