from django.contrib import admin
from .models import Contact, Category, News,Comment

admin.site.register(Contact)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_time', 'published_time')
    list_filter = ('status', 'category', 'created_time', 'published_time')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    search_fields = ('title', 'body')
    ordering = ('-status','-published_time')  # draftlar yuqorida chiqadi


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'author', 'body', 'created_time','active','updated_time')
    list_filter = ('active','news', 'author', 'created_time', 'updated_time')
    search_fields = ('body','author__username')
    ordering = ('-created_time','author__username')
    actions = ['disable_comment', 'enable_comment']
    def disable_comment(self, request, obj):
        obj.active = False
        obj.save()
    disable_comment.short_description = "Disable Comment"

    def enable_comment(self, request, obj):
        obj.active = True
        obj.save()
    enable_comment.short_description = "Enable Comment"

