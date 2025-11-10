from django.db import models
from django.utils.timezone import now

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_date = models.DateField(default=now)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(
        upload_to='book_covers/',  # rasm saqlanadigan papka
        blank=True,
        null=True,
        default='book_covers/default.jpg'  # default rasm
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
