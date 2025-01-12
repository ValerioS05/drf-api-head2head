from django.db import IntegrityError
from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    product = serializers.ReadOnlyField(source='product.id')
    is_owner = serializers.SerializerMethodField()
    def get_is_owner(self,obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Vote
        fields = [
            'id',
            'owner',
            'is_owner',
            'product',
            'vote',
            'created_at',
        ]

    