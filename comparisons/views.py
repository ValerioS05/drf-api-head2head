from rest_framework import generics, permissions
from .models import Comparison
from .serializers import ComparisonSerializer
from drf_api_head2head.permissions import IsOwnerOrReadOnly

class ComparisonList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ComparisonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer
