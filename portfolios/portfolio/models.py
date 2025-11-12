from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
# Create your models here.

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=150, unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

class AboutMe(models.Model):

    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    about_me=models.HTMLField(null=True, blank=True,help_text="Write something about yourself.")
    image=models.ImageField(upload_to='aboutme/iamges', null=True, blank=True)
    skills=models.ManyToManyField('Skill', blank=True,null=True, help_text="Select your skills.")
    my_name=models.CharField(max_length=100, help_text="Enter your name.")
    social_media=models.JSONField(null=True, blank=True, help_text="Enter your social media links in JSON format.") 

    def __str__(self):
        return self.my_name
    
class Education(models.Model):
    about_me=models.ForeignKey(AboutMe, on_delete=models.CASCADE,)
    start_year=models.IntegerField(max_length=4,help_text="Enter the start year.")
    end_year=models.IntegerField(max_length=4, help_text="Enter the end year.")
    degree=models.CharField(max_length=200, help_text="Enter the degree.")
    university=models.CharField(max_length=200, help_text="Enter the university name.") 
    description=models.TextField(null=True, blank=True, help_text="Enter the description.") 

    def __str__(self):
        return f"{self.degree} - {self.university}"
    

class Exprience(models.Model):
    about_me=models.ForeignKey(AboutMe, on_delete=models.CASCADE,)
    start_year=models.IntegerField(max_length=4, help_text="Enter the start year.")
    end_year=models.IntegerField(max_length=4, help_text="Enter the end year.")
    position=models.CharField(max_length=200, help_text="Enter the position.")
    company=models.CharField(max_length=200, help_text="Enter the company name.") 
    description=models.TextField(null=True, blank=True, help_text="Enter the description.") 

    def __str__(self):
        return f"{self.position} - {self.company}"

    

class Skill(models.Model):
    name=models.CharField(max_length=100, help_text="Enter the skill name.",unique=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title =models.CharField(max_length=200, help_text="Enter the project title.")
    year=models.IntegerField(max_length=4, help_text="Enter the project year.")
    client=models.CharField(max_length=200, help_text="Enter the client name.")
    service=models.CharField(max_length=200, help_text="Enter the service provided.")
    project_type=models.CharField(max_length=200, help_text="Enter the project type.")
    description=models.HTMLField(null=True, blank=True, help_text="Enter the project description.")
    image=models.ImageField(upload_to='projects/images', null=True, blank=True)
    slug=models.SlugField(max_length=200, unique=True, help_text="Enter the project slug for URL.") 
    is_active=models.BooleanField(default=False, help_text="Is the project active?")

#https://www.youtube.com/watch?v=EQX-_egWjZk&t=3776s