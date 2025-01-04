from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size must not be larger than 2MB.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width must be smaller than 4096px.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height must be smaller than 4096px.'
            )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'description',
            'price',
            'location',
            'image',
            'keywords',
            'features',
            'created_at',
            'owner',
        ]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0.')
        return value
    
    