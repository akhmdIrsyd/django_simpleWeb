from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Register your models here.
def _upload_path(instance, filename):
    return instance.get_upload_path(filename)


def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')

class kontak(models.Model):
    nama_kontak = models.CharField(max_length=50)
    email_kontak = models.CharField(max_length=50)
    isi_Kontak = models.TextField()
    tanggal=models.DateTimeField( auto_now=True, auto_now_add=False)
    def __str__(self):
        return str(self.nama_kontak)

class agenda(models.Model):
    nama_agenda = models.CharField(max_length=50)
    keterangan_agenda = models.TextField()
    tanggal_agenda=models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.nama_agenda)

class berita(models.Model):
    judul_berita = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    foto_berita = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['jpg']), file_size])
    isi_berita = models.TextField()
    tanggal=models.DateTimeField( auto_now=True, auto_now_add=False)
    def get_upload_path(self, filename):
        return "uploads/"+str(self.author.username)+"/"+filename
    def __str__(self):
        return str(self.judul_berita)

class galery(models.Model):
    foto_galery = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['jpg']), file_size])
    tanggal=models.DateTimeField( auto_now=True, auto_now_add=False)
    def get_upload_path(self, filename):
        return "uploads/"+str(galery)+"/"+filename