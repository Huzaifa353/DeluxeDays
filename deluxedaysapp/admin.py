from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Blog, HomeContent, Stat, GuestSectionContent, HostSectionContent, GuestSectionSlider, HostSectionSlider, Feedback, TeamMember, AboutSectionContent

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
class HostSectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class GuestSectionSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
class HostSectionSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'feedback', 'profile_image', 'created_at')

class AboutSectionContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'profile_image')


admin.site.register(Blog, BlogAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(GuestSectionContent, GuestSectionContentAdmin)
admin.site.register(HostSectionContent, HostSectionContentAdmin)
admin.site.register(GuestSectionSlider, GuestSectionSliderAdmin)
admin.site.register(HostSectionSlider, HostSectionSliderAdmin)
admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(AboutSectionContent, AboutSectionContentAdmin)
admin.site.register(TeamMember, TeamMembersAdmin)