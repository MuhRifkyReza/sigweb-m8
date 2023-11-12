from django.db import models

# Create your models here.
class Restoran(models.Model):
    nama = models.CharField(max_length=80)
    jenis = models.CharField(max_length=20)

    def __str__(self):
        return self.nama