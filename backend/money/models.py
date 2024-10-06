from django.db import models
from django.utils import timezone

from warehouse.models import Product

# Create your models here.
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_history = models.JSONField()

    def __str__(self):
        return self.product.name[:50]
    

class Promotion(models.Model):
    product = models.ForeignKey(Price, on_delete=models.CASCADE)
    rabat = models.DecimalField(default=0, decimal_places=0, max_digits=2)
    # users_grup = 

    def __str__(self):
        return f'{self.rabat}, {self.product.name[:50]}'