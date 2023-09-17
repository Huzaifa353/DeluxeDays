from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    content = models.TextField()
    read_duration = models.CharField(max_length=200, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Stat(models.Model):
    key = models.CharField(max_length=300)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"

class HomeContent(models.Model):
    key = models.CharField(max_length=300)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
    
class GuestSectionContent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Guest Section"
        verbose_name_plural = "Guest Section"