
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Hotel(models.Model):
    hotelname = models.CharField(max_length=40)
    hotelurl = models.URLField(blank=True)
    womanonly = models.CharField(max_length=3,default='')
    twosites = models.CharField(max_length=3,default='')
    nearstation = models.CharField(max_length=10)
    hotelprice = models.IntegerField(blank=True, validators=[MinValueValidator(1)])

    def publish(self):
        self.save()

    def __str__(self):
        return self.hotelname
