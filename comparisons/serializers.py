from rest_framework import serializers
from .models import Comparison
from products.models import Product

class ComparisonSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    is_owner = is_owner = serializers.SerializerMethodField()
    
    def validate_products(self, value):
        if len(value) != 2:
            raise serializers.ValidationError(
                'You must select exactly two products to compare.'
                )

        if value[0] == value[1]:
            raise serializers.ValidationError(
                "Can't compare the same product."
                )
        return value

    def get_is_owner(self,obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comparison
        fields = [
            'id',
            'owner',
            'is_owner',
            'products',
            'created_at',
        ]
    
    