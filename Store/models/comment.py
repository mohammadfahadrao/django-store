from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from . import Product
class Comment(models.Model):
    body = models.TextField(null=False, blank=False,validators=[MinLengthValidator(10)])
    user = models.ManyToManyField(User)
    product = models.ManyToManyField(Product)
