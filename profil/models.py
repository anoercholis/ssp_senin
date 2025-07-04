from django.db import models

# Create your models here.



class Jenis(models.Model):
    nama = models.CharField(max_length=20)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kdbrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=75)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150 , blank=True)
    tgl_input = models.DateTimeField(auto_now_add=True)
    id_jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama
    
    
class About(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.judul

class Feature(models.Model):
    pengantar = models.TextField()
    fet1 = models.CharField(max_length=75)
    isi_fet1=models.TextField()
    fet2=models.CharField(max_length=75)
    isi_fet2=models.TextField()
    img_fet=models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.pengantar