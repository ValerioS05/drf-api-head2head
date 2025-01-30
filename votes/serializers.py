from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        request = self.context['request']
        owner = request.user
        product = validated_data.get('product')
        existing_vote = Vote.objects.filter(
            owner=owner, product=product
            ).first()

        if existing_vote:
            existing_vote.vote = validated_data.get('vote', existing_vote.vote)
            existing_vote.save()
            return existing_vote
        else:
            return super().create(validated_data)

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
