from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import datetime

# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'blog/about.html', context)