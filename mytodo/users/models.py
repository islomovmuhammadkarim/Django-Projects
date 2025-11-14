from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    fanlar = models.TextField(blank=True, null=True)  # JSON yoki comma-separated string bo'lishi mumkin

    def __str__(self):
        return self.user.username
