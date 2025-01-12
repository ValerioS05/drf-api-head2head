from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from products.models import Product

class Vote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class Meta:
        ordering = [
            'owner',
            'product',
            '-created_at',
        ]
        unique_together = ('owner', 'product')
    
    def __str__(self):
        return f'{self.owner} voted on {self.product}.'
    
        
