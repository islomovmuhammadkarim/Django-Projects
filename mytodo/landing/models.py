from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from datetime import date
from django.utils import timezone

class About(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='images/')
    skills = models.TextField(help_text="Comma-separated skills")
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    expirence = models.TextField(help_text="Comma-separated experiences")

    social_twitter = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)
    social_github = models.URLField(blank=True, null=True)
    social_facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    message=HTMLField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"





class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def days_left(self):
        if self.deadline:
            delta = (self.deadline - timezone.localdate()).days
            return delta
        return None

    def __str__(self):
        return f"{self.title} ({self.user.username})"
