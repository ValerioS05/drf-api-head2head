from django.db import IntegrityError
from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    product = serializers.ReadOnlyField(source='product.id')
    class Meta:
        model = Vote
        fields = [
            'id',
            'owner',
            'product',
            'vote',
            'created_at',
        ]

    def validate_vote(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError(
                'Must be between 1 and 5.'
            )
        return value