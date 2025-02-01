from django.db import models
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from products.models import Product


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=200)
    profile_picture = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default_h2h'
    )
    favourites = models.ManyToManyField(
        Product, blank=True, related_name='favorited_by'
        )

    class Meta:
        ordering = [
            '-location',
        ]

    def __str__(self):
        return f"{self.owner}'s profile"

    def new_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(owner=instance)

    post_save.connect(new_user, sender=User)
