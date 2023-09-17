from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .models import Blog

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def blog(request):

    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)