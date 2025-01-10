from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from .models import Product

class CommentSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    created_at = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username')
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'product',
            'owner',
            'is_owner'
            'content',
            'created_at',
        ]