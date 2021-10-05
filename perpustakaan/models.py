from django.db import models


# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    jumlah = models.IntegerField(null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul
