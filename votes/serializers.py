from django.db import IntegrityError
from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self,obj):
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        product_id = self.initial_data.get('product')

        if not user or not product_id:
            raise serializers.ValidationError({'detail': 'User and product ID are required.'})

        try:
            existing_vote = Vote.objects.get(owner=user, product_id=product_id)
            existing_vote.vote = validated_data['vote']
            existing_vote.save()
            return existing_vote
        except Vote.DoesNotExist:
            pass

        try:
            return Vote.objects.create(owner=user, product_id=product_id, **validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'Possible duplicate vote'})

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