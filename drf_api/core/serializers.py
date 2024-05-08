from rest_framework import serializers
from .models import Kategori, Produk

# buat kelas serializer
class KategoriSerializer(serializers.ModelSerializer):
    produk = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Kategori
        fields = ["id", "nama", "produk"]

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ["id", "nama", "kategori"]
