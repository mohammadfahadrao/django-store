from django.urls import path
from Store.views import products,cart, createAndFetchCart
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', products, name='products'),
    path('cart/', cart, name='store'),
    path('cart/<int:id>/', createAndFetchCart, name='addToCart'),    

]
