from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Comparison(models.Model):
    product = models.ManyToManyField(Product, related_name='comparisons')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = [
            '-created_at',
            'owner',
        ]
    
    def __str__(self):
        product_names = ', '.join(
            [str(product) for product in self.products.all()]
        )
        return f"{self.owner} compared {product_names}"
