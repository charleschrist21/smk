from django.db import models
from siswa.models import siswa

absen=(
    ('M', 'Masuk'),
    ('A','alpa'),
    ('I','IZIN'),
    ('S', 'SAKIT'),
    ('L', 'Libur')
)
bulan=(
    ('Januari', 'Januari'),
    ('Februari', 'Februari'),
    ('Maret', 'Maret'),
    ('April','April'),
    ('Mei', 'Mei'),
    ('Juni', 'Juni'),
    ('Juli','Juli'),
    ('Agustus','Agustus'),
    ('September','September'),
    ('Oktober','Oktober'),
    ('November','November'),
    ('Desember', 'Desember'),

)


class tanggalAbsen(models.Model):
    class Meta:
        db_table = 'tanggalAbsen'

    tgl_1 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_2 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_3 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_4 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_5 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_6 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_7 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_8 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_9 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_10 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_11 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_12 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_13 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_14 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_15 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_16 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_17 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_18 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_19 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_20 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_21 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_22 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_23 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_24 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_25 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_26 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_27 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_28 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_29 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_30 = models.CharField(choices=absen ,null=True, max_length=10)
    tgl_31 = models.CharField(choices=absen ,null=True, max_length=10)


class bulanAbsen(models.Model):
    class Meta:
        db_table = 'bulanAbsen'

    Bulan = models.CharField(choices=bulan, max_length=255)
    tanggal = models.ForeignKey(tanggalAbsen, on_delete=models.CASCADE)
    nama_siswa = models.ForeignKey(siswa, on_delete=models.CASCADE)

    def __str__(self):
        return self.Bulan
