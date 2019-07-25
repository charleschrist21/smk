from django.db import models
from siswa.models import siswa

class tagihan(models.Model):
    class Meta:
        db_table = 'tagihanSiswa'
    
    spp = models.CharField(null=True,blank=True,max_length=255)
    osis = models.CharField(null=True,blank=True,max_length=255)
    lain1 = models.CharField("Lain-lain", null=True, blank=True,max_length=255)
    lain2 = models.CharField("Lain-lain",null=True,blank=True,max_length=255)
    lain3 = models.CharField("Lain-lain",null=True,blank=True,max_length=255)
    lain4 = models.CharField("Lain-lain",null=True,blank=True,max_length=255)
    lain5 = models.CharField("Lain-lain",null=True,blank=True,max_length=255)
    lain6 = models.CharField("Lain-lain",null=True,blank=True,max_length=255)
    lain7 = models.CharField("Lain-lain",null=True,blank=True,max_length=255)
    namaSiswa = models.CharField(siswa,max_length=255)
    
    def __str__(self):
        return self.spp
