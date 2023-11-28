from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError 
# Create your models here.


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=20)


