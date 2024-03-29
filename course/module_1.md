# MODULE 1 - DRF - INSTALASI

Untuk dapat memahami proses dari keseluruhan modul ini, maka perlu untuk melakukan proses pada tahap pertama ini.

### Persiapan dan Instalasi
1. Clone proyek yang ada pada repository ini atau buat proyek baru.
```
git clone https://github.com/rofiuddin15/drf_course_backend.git
cd drf_course_backend
```
2. Jika membuat proyek baru maka abaikan perintah di atas dan jalankan perintah berikut.
- untuk windows
```
python -m venv myenv
myenv\Scripts\activate
```
- untuk Linux dan Mac
```
python3 -m venv myenv
source myenv\bin\activate
```
3. Copy daftar paket berikut kedalam file ```requirements.txt``` dan tempatkan sejajar dengan folder myenv.
```
asgiref==3.8.1
Django==5.0.3
django-extensions==3.2.3
django-filter==24.1
djangorestframework==3.15.1
djangorestframework-jsonapi==6.1.0
inflection==0.5.1
python-dotenv==1.0.1
pytz==2024.1
sqlparse==0.4.4
tzdata==2024.1
```
4. Jalankan perintah berikut
```
pip install -r requirements.txt
```
### Instalasi Django
5. Proses berikutnya adalah pemasangan django dan applikasi baru. Untuk itu jalankan kode berikut pada terminal.
```
django-admin startprojects drf_api
```
- Buat App baru dengan menjalankan perintah berikut.
```
cd drf_api
python manage.py startapp core
```
Sampai disini proses untuk persiapan module berikutnya sudah selesai. Tes hasil duplikat proyek atau proyek baru kita dengan menjalankan proyek.
```
python manage.py runserver
```
Dan selamat! kita sudah menyelesaikan satu module.