from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB','Published'
        DRAFT = 'D','Draft'
    
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=News.Status.PUBLISHED)

    title = models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    body=RichTextField()
    image=models.ImageField(upload_to='news/images')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    published_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    
  
    objects = models.Manager()  # Default manager
    published = PublishedManager()
    
    
    
    class Meta:
        ordering = ['-created_time']
    

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("news-detail", args=[self.slug])
    
    
class Comment(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    body=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']
    
    def __str__(self):
        return self.body