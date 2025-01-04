from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from drf_api_head2head.permissions import IsOwnerOrReadOnly

class ProductList(APIView):
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer_class = ProductSerializer
        serializer = ProductSerializer(
            data=request.data,
            context={
                'request' : request
            }
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProductDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_product(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        product = self.get_product(pk)
        self.check_object_permissions(self.request, product)
        serializer = ProductSerializer(
            product,
            context= {
                'request' : request
            }
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_product(pk)
        self.check_object_permissions(self.request, product)
        serializer = ProductSerializer(
            product,
            data = request.data,
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
        product = self.get_product(pk)
        self.check_object_permissions(self.request, product)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)