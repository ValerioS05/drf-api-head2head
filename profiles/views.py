from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_head2head.permissions import IsOwnerOrReadOnly, IsStaffUser
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'bio',
        'location',
        'favourite'
    ]
    ordering_fields = [
        'owner__username',
        'location',
    ]
    filterset_fields = [
        'location',
        'owner__username',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly | IsStaffUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_update(self, serializer):
        profile_picture = self.request.FILES.get('profile_picture', None)
        if profile_picture:
            serializer.validated_data['profile_picture'] = profile_picture
            serializer.save()
