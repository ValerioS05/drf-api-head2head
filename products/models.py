from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
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
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = [
            'name',
            'location',
            '-category__name',
            '-price',
        ]

    def __str__(self):
        return f'{self.name} from {self.owner} ,(£{self.price})'

    def get_average_rating(self):
        votes = self.votes.all()
        if votes.exists():
            return votes.aggregate(models.Avg('vote'))['vote__avg']
        return None
