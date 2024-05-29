from Store.models import Product, CartItem
from django.shortcuts import get_object_or_404
import pdb
def upsert_session_cart(request, id):
    cart = request.session.get('cart',{})

    product = get_object_or_404(Product, id=id)
    product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1
        }
    pid = str(product.id)
    if pid in cart:
        cart[pid]['quantity'] += 1
    else:
        cart[pid] = product_data
    
    request.session['cart'] = cart
    request.session.modified = True 

    return cart

def delete_cart_item(request, id):
    cart = request.session.get("cart")
    cart.pop(str(id))
    request.session['cart'] = cart
    request.session.modified = True 
    return cart