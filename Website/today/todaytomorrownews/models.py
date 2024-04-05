from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError 
# Create your models here.


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=20)



class News(models.Model):
    nid=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.title

class Category(models.Model):
    nid = models.ForeignKey(News, on_delete=models.CASCADE, related_name='categories')
    cat = models.CharField(max_length=50)
    def __str__(self):
        return self.cat


