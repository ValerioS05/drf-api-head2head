from rest_framework import serializers
from .models import Comment
from .moldels import Product

class CommentSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.id')
    created_at = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = [
            'id',
            'product',
            'owner',
            'content',
            'created_at',
        ]