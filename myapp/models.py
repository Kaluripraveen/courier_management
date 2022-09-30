from asyncio import AbstractServer
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    FristName = models.CharField(max_length=225, default='praveen')
    LastName = models.CharField(max_length=225, default='k')
    email = models.CharField(max_length=255 , unique=True)
    password = models.CharField(max_length=255)
    username= None
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
    