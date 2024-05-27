from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    status = models.BooleanField(null=False, blank=False,default=False)
    amount_total = models.DecimalField( max_digits=5, decimal_places=2,null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

