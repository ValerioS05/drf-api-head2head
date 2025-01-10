from django.db import IntegrityError
from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    product = serializers.ReadOnlyField(source='product.id')
    is_owner = serializers.SerializerMethodField()

    def validate_vote(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError(
                'Must be between 1 and 5.'
            )
        return value

    class Meta:
        model = Vote
        fields = [
            'id',
            'owner',
            'is_owner'
            'product',
            'vote',
            'created_at',
        ]

    