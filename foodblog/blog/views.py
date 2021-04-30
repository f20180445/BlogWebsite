from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

posts = [
    {
        'author': 'Jainam',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '30th April, 2021'
    },
    {
        'author': 'Niyati',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2nd May, 2021'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': "Home"
    }
    return render(request, "blog/home.html", context)

def about(request):
    context = {
        'title': "About"
    }
    return render(request, "blog/about.html", context)

def contact_us(request):
    return render(request, "blog/SurveyForm.html")
# Create your views here.
