from .models import *
from django.shortcuts import render

def printindex(request):
    return render(request, "index.html")


def categori_list(request):
    categories = Category.objects.all()
    return render(request, 'categori.html', {'categories': categories})

def product(request):
    products = Product.objects.all()
    return render(request,'Product.html',{'products':products})

def review(request):
    reviews = Review.objects.all()
    return render(request,"Review.html",{"reviews":reviews})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


