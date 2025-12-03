from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio', 'location', 'birth_date')
    list_filter = ('user', 'bio', 'location', 'birth_date')
    search_fields = ('user', 'bio', 'location', 'birth_date')
    ordering = ('user', 'bio', 'location', 'birth_date')

admin.site.register(Profile, ProfileAdmin)