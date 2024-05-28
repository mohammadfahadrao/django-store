from django.db import models
from django.core.validators import MinValueValidator,MinLengthValidator
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.TextField(validators=[MinLengthValidator(3)],blank=False, null=False)
    description = models.TextField(validators=[MinLengthValidator(10)],blank=False, null=False)
    price = models.FloatField(MinValueValidator(1), null=False, blank=False)
    stock = models.IntegerField(MinValueValidator(1), null=False, blank=False)
    product_picture = models.FileField(upload_to="uploads/", default=' ')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.description}"
