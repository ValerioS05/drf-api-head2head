from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from drf_api_head2head.permissions import IsStaffUser

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffUser]

    def perform_create(self, serializer):
        serializer.save()

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffUser]