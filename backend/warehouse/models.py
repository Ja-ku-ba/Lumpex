from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added']
    
    def __str__(self):
        return self.name
    

class ProductFiles(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=timezone.now)
    # file = models.FileField()

    def __str__(self):
        return f'{self.product[:50]}, {self.id}'