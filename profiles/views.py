from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from drf_api_head2head.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer