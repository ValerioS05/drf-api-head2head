from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model) :
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default_h2h'
    )

    def clean(self):
        """
        Simple validation for image size, format, and dimensions.
        """

        max_size = 5 * 1024 * 1024
        if self.image.size > max_size:
            raise ValidationError('Image size must be less than 5MB.')

        formats = ('.png', '.jpg', '.jpeg')
        if not self.image.name.endswith(formats):
            raise ValidationError('Image must be in .png, .jpg, .jpeg format.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name