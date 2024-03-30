# MODULE 4 - DRF - SERIALIZER

Pada module ini kita bahas tentang serializer. Serializer merupakan Model untuk membentuk keluaran berupa Rest API berupa JSON, XML atau lainnya. Serializer bekerja seperti Django Form atau ModelForm, cara yang sangat ajaib yang disediakan oleh DRF. Oke mari kita mulai.
## Membuat Serializer
- Buatlah file di dalam modul atau App core dengan nama ``serializers.py``
- Isi file tersebut dengan kode berikut
```
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
```
### Keterangan
1. Pada baris pertama kita import class ``serializers`` yang mana module ini kita gunakan layaknya model form pada django.
```
from rest_framework import serializers
```
2. Baris kedua kita import model yang sudah kita buat sebelumnya.
```
from .models import Kategori, Produk
```
3. Buat Kelas serializer dengan nama disesuaikan dengan nama modelnya. Disi kita buat dua buah untuk model Kategori dan Produk, kelas tersebut inherit atau mewarisi model ModelSerializer yang datang dari module serializers.
```
class KategoriSerializer(serializers.ModelSerializer):
    ....
```
4. Kelas Meta di dalam kelas ProdukSerializer merupakan meta data atau penegasan terhadap model dan field yang ada pada masing-masing model.
```
class Meta:
    model = Kategori
    fields = ["id", "nama"]
```