# MODULE 2 - DRF - KONFIGURASI
Untuk dapat menggunakan Django Rest Framework (DRF), kita perlu untuk melakukan proses konfigurasi. Proses ini sangat penting agar paket DRF dan kebutuhan lainnya yang sudah kita pasang pada sistem Django dapat kita gunakan.
## Konfigurasi DRF
1. Daftarkan paket rest framework pada file ```settings.py``` pada folder proyek drf_api.
```
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]
```
2.  Daftarkan default permission, pasang di akhir kode pada ```settings.py```
```
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```
3. Daftarkan URL auth rest framework pada file ```urls.py``` pada folder proyek drf_api.
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
```
Dan selesai! kita dapat mencobanya dengan mengakses url di atas, tetapi aplikasi kita belum sepenuhnya dapat di gunakan. Untuk dapat menggunakan aplikasi kita secara utuh kita lanjutkan pada module berikutnya.