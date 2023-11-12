from django.db import models

# Create your models here.

from django.contrib.gis.db import models


class BangunanPogung(models.Model):
    nama = models.CharField(max_length=254, null=True, blank=True)
    jenis = models.CharField(max_length=254, null=True, blank=True)
    pemilik = models.ForeignKey("peta.Restoran", on_delete=models.CASCADE, max_length=10, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
