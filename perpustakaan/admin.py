from django.contrib import admin
from perpustakaan.models import Buku,Kategori

# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','penerbit','kategori','jumlah']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ['kategori_id']
    list_per_page = 10

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kategori)
