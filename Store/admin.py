from django.contrib import admin
from .models import  CartItem, Product, Comment, Order, OrderItem
from django.contrib import admin
from .models import Comment, CartItem

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'get_users', 'get_products']

    def get_users(self, obj):
        return ", ".join([str(user) for user in obj.user.all()])
    get_users.short_description = 'Users'

    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.product.all()])
    get_products.short_description = 'Products'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'get_products', 'get_users')

    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.product.all()])
    get_products.short_description = 'Products'

    def get_users(self, obj):
        return ", ".join([str(user) for user in obj.user.all()])
    get_users.short_description = 'Users'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
'description',
'price',
'stock',
'owner']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status',
'amount_total',
'user']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_qty','order_id']