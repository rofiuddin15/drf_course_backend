from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama