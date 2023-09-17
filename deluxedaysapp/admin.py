from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'read_duration', 'published_date')

admin.site.register(Blog, BlogAdmin)