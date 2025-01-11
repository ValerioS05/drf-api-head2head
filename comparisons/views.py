from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comparison
from .serializers import ComparisonSerializer
from drf_api_head2head.permissions import IsOwnerOrReadOnly

class ComparisonList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'products__id'
    ]
    ordering_fields = [
        'created_at',
        'owner__username',
    ]
    filterset_fields = [
        'owner__username',
        'products',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ComparisonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer