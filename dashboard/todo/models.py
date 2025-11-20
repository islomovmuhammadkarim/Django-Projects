# todo/models.py
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Vazifa sarlavhasi
    title = models.CharField(max_length=200)
    
    # Ustuvorlik tanlovlari
    PRIORITY_CHOICES = [
        ('high', 'Yuqori'),
        ('medium', 'Oʻrta'),
        ('low', 'Past'),
    ]
    priority = models.CharField(max_length=10, 
                                choices=PRIORITY_CHOICES, 
                                default='medium')
                                
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Admin paneli va boshqa joylar uchun title ni qaytaramiz
        return self.title
        
    class Meta:
        ordering = ['-created_at']


class TimeCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # foydalanuvchi bilan bog'lash
    name = models.CharField(max_length=100)                  # soha nomi
    total_minutes = models.PositiveIntegerField(default=0)   # jami vaqt (minutlarda)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'name')  # foydalanuvchi uchun noyob nom

    def __str__(self):
        return f"{self.name} ({self.total_minutes} min)"
