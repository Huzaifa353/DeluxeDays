from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Blog, HomeContent, Stat, GuestSectionContent

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'read_duration', 'published_date')
class StatAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
class GuestSectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(GuestSectionContent, GuestSectionContentAdmin)