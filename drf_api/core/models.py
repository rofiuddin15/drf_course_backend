from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, related_name="produk", on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama