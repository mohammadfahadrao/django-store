from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from . import Product


class CartItem(models.Model):
    quantity = models.IntegerField(MinValueValidator(1))
    product = models.ManyToManyField(Product)
    user = models.ManyToManyField(User)