from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .models import Blog, HomeContent, Stat, GuestSectionContent, HostSectionContent, GuestSectionSlider, HostSectionSlider, Feedback, TeamMember, AboutSectionContent

# Create your views here.

def index(request):

    context = {
        'title': HomeContent.objects.get(key='Header Title').value,
        'description': HomeContent.objects.get(key='Header Description').value,
        'accomodations': Stat.objects.get(key='Accomodations').value,
        'cars': Stat.objects.get(key='Cars').value,
        'boats': Stat.objects.get(key='Boats').value,
        'users': Stat.objects.get(key='Trusted Users').value,
        'experiences': Stat.objects.get(key='Experiences').value,
        'hosts': Stat.objects.get(key='Verified Hosts').value,
        's1Title': HomeContent.objects.get(key='Section 1 Title').value,
        's1Description': HomeContent.objects.get(key='Section 1 Description').value,
        'guestSections': GuestSectionContent.objects.all(),
        'hostSections': HostSectionContent.objects.all(),
        'guestSliders': GuestSectionSlider.objects.all(),
        'guestSliderTitle': HomeContent.objects.get(key="Guest Slider Title").value,
        'hostSliders': HostSectionSlider.objects.all(),
        'hostSliderTitle': HomeContent.objects.get(key="Host Slider Title").value,
        'feedbacks': Feedback.objects.all(),
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    context = {
        'aboutSections': AboutSectionContent.objects.all(),
        'teamMembers': TeamMember.objects.all()
    }
    return render(request, 'about.html', context)


def blog(request):

    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)