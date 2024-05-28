from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Store.models import Product, CartItem
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from Store.services.product import upsert_session_cart
import pdb


def products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html',{'products': products})

@login_required(login_url='/')
def cart(request):
    cart_items = CartItem.objects
    return render(request, 'store/cart.html')

def createAndFetchCart(request, id):
    
    cart = upsert_session_cart(request,id)
    return render(request, 'store/cart.html', {'cart': cart})

    