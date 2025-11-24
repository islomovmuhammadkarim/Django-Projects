from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age=models.PositiveBigIntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    
    