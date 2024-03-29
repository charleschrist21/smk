# Generated by Django 2.2.3 on 2019-07-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='siswa',
            fields=[
                ('nis', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('alamat', models.TextField(max_length=500)),
                ('jurusan', models.CharField(choices=[('TKJ', 'TKJ'), ('MM', 'MM'), ('PDR', 'PDR'), ('OTKP', 'OTKP'), ('AKL', 'AKL'), ('PM', 'PM'), ('PS', 'PS')], max_length=255, verbose_name='Jurusan')),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('tanggal_lahir', models.CharField(max_length=255)),
                ('Agama', models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katolik', 'Katolik'), ('Budha', 'Budha'), ('Hindu', 'Hindu'), ('Konghucu', 'Konghucu'), ('Lainnya', 'Lainnya')], max_length=255)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan'), ('Lainnya', 'Lainnya')], max_length=255)),
                ('kelas', models.CharField(choices=[('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], max_length=255)),
                ('no_telpon', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'siswas',
            },
        ),
    ]
