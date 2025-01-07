from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from drf_api_head2head.permissions import IsOwnerOrReadOnly
from .models import Vote
from .serializers import VoteSerializer

class VoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        if not product_id:
            raise ValidationError({'product': 'This field is required.'})
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError({'product': 'Invalid product ID.'})
        serializer.save(owner=self.request.user, product=product)


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()