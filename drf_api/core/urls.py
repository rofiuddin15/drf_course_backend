from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('kategori/', views.kategori_list),
    path('kategori/<int:pk>/', views.kategori_detail),
    path('produk/', views.ProdukList.as_view()),
    path('produk/<int:pk>/', views.ProdukDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
