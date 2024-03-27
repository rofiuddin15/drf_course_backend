from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Kategori, Produk
from .serializers import KategoriSerializer, ProdukiSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def kategori_list(request, format=None):

    if request.method == 'GET':
        kategori = Kategori.objects.all()
        serializer = KategoriSerializer(kategori, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def kategori_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        kategori = Kategori.objects.get(pk=pk)
    except Kategori.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KategoriSerializer(kategori)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)