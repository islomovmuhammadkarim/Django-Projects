# app_name/admin.py
from django.contrib import admin
from .models import Todo, TimeCategory

class TodoAdmin(admin.ModelAdmin):
    # Bu nomlar models.py dagi maydonlarga to'liq mos kelishi shart
    list_display = ('title', 'priority', 'completed') 
    list_filter = ('priority', 'completed')           
    search_fields = ('title',)                        
    list_editable = ('completed',)                    

admin.site.register(Todo, TodoAdmin)

admin.site.register(TimeCategory)
