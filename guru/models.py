from django.db import models

pangkat=(
    ('Kepsek', 'Kepsek'),
    ('Guru', 'Guru'),
    ('Guru kejuruan', 'Guru Kejuruan')
)
status=(
    ('pns','pns'),
    ('non pns', 'non pns')
)
mapel=(
    ('mtk','mtk'),
    ('bahasa indonesia','bahasa indonesia'),
    ('bahasa inggris', 'bahasa inggris'),
    ('bahasa jawa', 'bahasa jawa'),
    ('jurusan', 'jurusan')
)


class Guru(models.Model):
    class Meta:
        db_table = 'guru'

    nip = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    tanggal_lahir = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    pangkat = models.CharField(max_length=100, choices=pangkat)
    status = models.CharField(max_length=100, choices=status)
    tanggal_masuk = models.CharField(max_length=255)
    mapel1 = models.CharField(max_length=100, choices=mapel)
    mapel2 = models.CharField(max_length=100, null=True, blank=True, choices=mapel)
    mapel3 = models.CharField(max_length=100, null=True, blank=True, choices=mapel)
    mapel4 = models.CharField(max_length=100, null=True, blank=True, choices=mapel)
    mapel5 = models.CharField(max_length=100, null=True, blank=True, choices=mapel)
    pendidikan = models.CharField(max_length=100)
    umur = models.CharField(max_length=100)
    file = models.FileField("image", null=True,blank=True)
    
    def __str__(self):
        return self.full_name