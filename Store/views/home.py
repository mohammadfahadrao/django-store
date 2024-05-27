from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Store.models import Product

def products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html',{'products': products})

def store(request):
    return render(request, 'store/cart.html')
    