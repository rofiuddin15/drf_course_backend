# MODULE 3 - DRF - MODEL
Pada module ini lakukan perubahan pada model dari App yang sebelumnya sudah kita buat. Tujuannya adalah untuk mempersiapkan data model sebagai penyimpanan, model pada django bertugas sebagai perantara koneksi ke database sekaligus pembentuk migration. Migration sendiri merupakan cetak biru data tabel.
## Membuat Struktur Data
Sebagai contoh kita akan membuat API untuk aplikasi penjualan, disini kita butuh beberapa tabel, dan sebagai contoh dasar kita buat dua, yaitu:
* Kategori Produk
* Produk

Selanjutnya kita buat model pada file ``models.py``
```
class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
```
Simpan dan jalankan perintah berikut untuk membentuk migrations.
```
python manage.py makemigrations
python manage.py migrate
```
Selesai! proses pembuatan model sudah berhasil. Ini masih permulaan, selanjutnya buat sebuah serialization, proses ini kita akan bahas pada module berikutnya.

Selamat mencoba!