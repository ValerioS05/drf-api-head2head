from django.db.models import Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_head2head.permissions import IsOwnerOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.annotate(
        average_rating=Avg('votes__vote')
    )

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'name',
        'keywords',
        'category__name',
        'owner__username'
    ]
    ordering_fields = [
        'name',
        'price',
        'created_at',
        'average_rating',
    ]
    filterset_fields = [
        'category',
        'price',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
