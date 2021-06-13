from django.db import models
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

