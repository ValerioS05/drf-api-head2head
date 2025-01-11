from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            '-created_at'
        ]
    
    def __str__(self):
        return f"{self.owner} commented on {self.product}."
