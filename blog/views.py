from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Myint Myat Kaung',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 11, 2018'
    },
    {
        'author': 'Mg Kaung',
        'title': 'Blog Post 2',
        'content': 'Secont post content',
        'date_posted': 'August 21, 2018'
    },
]


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
