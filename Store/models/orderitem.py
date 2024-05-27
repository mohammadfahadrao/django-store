from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MinLengthValidator
from . import Order

class OrderItem(models.Model):
    product_name = models.TextField(validators=[MinLengthValidator(3)],blank=False, null=False)
    product_price = models.TextField(validators=[MinLengthValidator(3)],blank=False, null=False)
    product_qty = models.IntegerField(MinValueValidator(1))
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

