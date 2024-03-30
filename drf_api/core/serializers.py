from rest_framework import serializers
from .models import Kategori, Produk

# buat kelas serializer
class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ["id", "nama"]

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ["id", "nama"]