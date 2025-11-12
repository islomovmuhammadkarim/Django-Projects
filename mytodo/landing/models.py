from django.db import models
from django.contrib.auth.models import User



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
    