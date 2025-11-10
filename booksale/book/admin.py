from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'available', 'published_date', 'cover_image')
    list_filter = ('available', 'published_date')
    search_fields = ('title', 'author')
