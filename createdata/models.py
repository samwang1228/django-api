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

class User_login(models.Model): #登入與註冊
    user_id=models.CharField(max_length=45)
    password =models.CharField(max_length=20)
    nickname = models.CharField(max_length=50)
    login_check=BooleanField(default=False)

class Room_detail(models.Model): #留言
    user_id=models.CharField(max_length=45)
    nickname = models.CharField(max_length=50)
    cotent = models.TextField(blank=True)
    room_title = models.CharField(max_length=45)
    room_id= models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    room_title=models.CharField(max_length=45)
    room_id=models.CharField(max_length=50)

class Numbers_room(models.Model): #右側伺服器人員
    nickname = models.CharField(max_length=50)
    user_id = models.CharField(max_length=45)
    room_id = models.CharField(max_length=45)
    

class Numbers(models.Model):
    room_id = models.CharField(max_length=45)
    user_id = models.ForeignKey(User_login, on_delete=models.CASCADE, null=True)

class Blog(models.Model):
    name = models.CharField(max_length=100)
class Entry(models.Model):
    blog = models.ForeignKey(Blog ,on_delete=models.CASCADE, null=True)
    headline = models.CharField(max_length=255)


class Restaurant(models.Model):
    name = models.CharField(max_length=200)

class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


