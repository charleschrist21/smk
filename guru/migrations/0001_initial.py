# Generated by Django 2.2.3 on 2019-07-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('nip', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('tanggal_lahir', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('pangkat', models.CharField(choices=[('Kepsek', 'Kepsek'), ('Guru', 'Guru'), ('Guru kejuruan', 'Guru Kejuruan')], max_length=100)),
                ('status', models.CharField(choices=[('pns', 'pns'), ('non pns', 'non pns')], max_length=100)),
                ('tanggal_masuk', models.CharField(max_length=255)),
                ('mapel1', models.CharField(choices=[('mtk', 'mtk'), ('bahasa indonesia', 'bahasa indonesia'), ('bahasa inggris', 'bahasa inggris'), ('bahasa jawa', 'bahasa jawa'), ('jurusan', 'jurusan')], max_length=100)),
                ('mapel2', models.CharField(blank=True, choices=[('mtk', 'mtk'), ('bahasa indonesia', 'bahasa indonesia'), ('bahasa inggris', 'bahasa inggris'), ('bahasa jawa', 'bahasa jawa'), ('jurusan', 'jurusan')], max_length=100, null=True)),
                ('mapel3', models.CharField(blank=True, choices=[('mtk', 'mtk'), ('bahasa indonesia', 'bahasa indonesia'), ('bahasa inggris', 'bahasa inggris'), ('bahasa jawa', 'bahasa jawa'), ('jurusan', 'jurusan')], max_length=100, null=True)),
                ('mapel4', models.CharField(blank=True, choices=[('mtk', 'mtk'), ('bahasa indonesia', 'bahasa indonesia'), ('bahasa inggris', 'bahasa inggris'), ('bahasa jawa', 'bahasa jawa'), ('jurusan', 'jurusan')], max_length=100, null=True)),
                ('mapel5', models.CharField(blank=True, choices=[('mtk', 'mtk'), ('bahasa indonesia', 'bahasa indonesia'), ('bahasa inggris', 'bahasa inggris'), ('bahasa jawa', 'bahasa jawa'), ('jurusan', 'jurusan')], max_length=100, null=True)),
                ('pendidikan', models.CharField(max_length=100)),
                ('umur', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='image')),
            ],
            options={
                'db_table': 'guru',
            },
        ),
    ]
