from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

#ini adalah extend dari class User. Isinya berkaitan dengan siapa yang logged in
class People(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    nama = models.TextField()
    role = models.IntegerField()    

class Pelanggan(models.Model):
    nama_perusahaan = models.TextField()
    alamat = models.TextField()
    kota = models.TextField()
    telpon = models.TextField()
    #TODO: supervisor nama dan telpon

class Cabang(models.Model):
    nama = models.TextField()
    alamat = models.TextField()

class AkunBank(models.Model):
    nama_bank = models.TextField()
    nomor_rekening = models.TextField()
    nama_pemilik = models.TextField()    


