from django.urls import path
from Store.views import products
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', products, name='products'),
]
