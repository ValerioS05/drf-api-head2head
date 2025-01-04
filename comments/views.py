from django.http import Http404
from rest_framework import status, permissions
from rest_framework import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from drf_api_head2head.permissions import IsOwnerOrReadOnly

class CommentList(APIView):
    serializer_class = CommentSerializer
    permissions_classes = [
        permission.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(
            comments,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(
                'You must be logged in to leave a comment.',
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = CommentSerializer(
            data=request.data,
            context={
                'request' : request
            }
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CommentDetail(APIView):
    permissions_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    
    def get_comment(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_comment(pk)
        self.check_object_permissions(self.request, comment)
        serializer = CommentSerializer(
            comment,
            context= {
                'request' : request
            }
        )
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_comment(pk)
        self.check_object_permissions(self.request, comment)
        serializer = CommentSerializer(
            comment,
            data=request.data,
            context = {
                'request' : request
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, pk):
        comment = self.get_comment(pk)
        self.check_object_permissions(self.request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        