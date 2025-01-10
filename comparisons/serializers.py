from rest_framework import serializers
from .models import Comparison
from products.models import Product

class ComparisonSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    def validate_products(self, value):
        if len(value) != 2:
            raise serializers.ValidationError(
                'You must select exactly two products to compare.'
                )
        return value
        if value[0] == value[1]:
            raise serializers.ValidationError(
                "Can't compare the same product."
                )
        return value

    class Meta:
        model = Comparison
        fields = [
            'id',
            'owner',
            'products',
            'created_at',
        ]
    
    