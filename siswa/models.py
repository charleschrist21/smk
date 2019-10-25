from django.db import models


jurusan =(
    ('TKJ', 'TKJ'),
    ('MM', 'MM'),
    ('PDR', 'PDR'),
    ('OTKP', 'OTKP'),
    ('AKL', 'AKL'),
    ('PM', 'PM'),
    ('PS','PS'),
)
kelas =(
    ('X', 'X'),
    ('XI','XI'),
    ('XII', 'XII')
)
jenisKelamin=(
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan','Perempuan'),
    ('Lainnya', 'Lainnya')
)
agama =(
    ('Islam', 'Islam'),
    ('Kristen', 'Kristen'),
    ('Katolik', 'Katolik'),
    ('Budha', 'Budha'),
    ('Hindu', 'Hindu'),
    ('Konghucu', 'Konghucu'),
    ('Lainnya', 'Lainnya')
)


class siswa(models.Model):
    class Meta:
        db_table = 'siswas'

    nis = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    alamat = models.TextField(max_length=500)
    jurusan = models.CharField("Jurusan",max_length=255,choices=jurusan)
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.CharField(max_length=255, null=False)
    Agama = models.CharField(max_length=255,choices=agama)
    jenis_kelamin = models.CharField(max_length=255,choices=jenisKelamin)
    kelas = models.CharField(max_length=255, choices=kelas)
    no_telpon = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    file = models.FileField("Image",null=True, blank=True)
    


    def __str__(self):
        return self.full_name



