from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    average_rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.profile.profile_picture.url')
    vote_id = serializers.SerializerMethodField()
    
    def get_is_owner(self,obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0.')
        return value

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_vote_id(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            vote = Vote.objects.filter(owner=request.user, product=obj).first()
            return vote.id if vote else None
        return None
    
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
            'is_owner',
            'average_rating',
            'profile_id',
            'profile_picture',
            'vote_id',
        ]
