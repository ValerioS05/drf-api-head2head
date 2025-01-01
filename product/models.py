from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .models import Profile
from .models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
        )   
    location = models.CharField(max_length=250)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default_h2h'
    )
    keywords = models.TextField(
        validators=[MaxLengthValidator(600)]
    )
    features = models.TextField(
        validators=[MaxLengthValidator(450)]
    )
    created_at = models.DateField()
    creator = models.ForeignKey(User)
    
    class Meta:
        order = [
            'name',
            'location',
            '-category__name',
            '-price',
        ]

    def __str__(self):
        return f'{self.name}, {self.category} from {self.creator} ({self.price})'
    