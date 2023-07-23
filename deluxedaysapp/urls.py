from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contactus/',views.contact,name='contactus'),
    path('aboutus/',views.about,name='aboutus'),
    path('blogs/',views.blog,name='blogs')
]
