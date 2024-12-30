from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model) :
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='../default_h2h'
    )
    
    def __str__(self):
        return self.name