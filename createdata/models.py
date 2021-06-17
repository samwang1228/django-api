from django.db import models
from django.db.models.fields import BooleanField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField(blank=True)
    photo=models.URLField(blank=True)
    location = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    user_id=models.CharField(max_length=45)
    nickname = models.CharField(max_length=50)
    password =models.CharField(max_length=20)

class User_login(models.Model):
    user_id=models.CharField(max_length=45)
    password =models.CharField(max_length=20)
    nickname = models.CharField(max_length=50)
    login_check=BooleanField(default=False)

class Room_detail(models.Model):
    user_id=models.CharField(max_length=45)
    nickname = models.CharField(max_length=50)
    cotent = models.TextField(blank=True)
    room_title = models.CharField(max_length=45)
    room_id= models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    room_title=models.CharField(max_length=45)
    room_id=models.CharField(max_length=50)
    


