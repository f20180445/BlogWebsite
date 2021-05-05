from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Post, Product

def home(request):
    context = {
        'posts': Post.objects.all(),
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

def products(request):
    context={
        "first_product":Product.objects.first(),
        "products":Product.objects.all(),
        "title":"Products"
    }
    print(Product.objects.first())
    return render(request, "blog/products.html", context)
# Create your views here.
