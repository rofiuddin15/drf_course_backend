from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Kategori, Produk
from .serializers import KategoriSerializer, ProdukSerializer

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

# view untuk produk dengan class base view
class ProdukList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        produk = Produk.objects.all()
        serializer = ProdukSerializer(produk, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Produk.objects.get(pk=pk)
        except Produk.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        produk = self.get_object(pk=pk)
        produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)