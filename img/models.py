from django.db import models
from django import forms
from PIL import *
# Create your models here.
class imagess(models.Model):
    picture = models.ImageField(upload_to = 'stati')
    comment = models.CharField(max_length = 200)
    mood = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    lat = models.FloatField()
    lon = models.FloatField()
class t(models.Model):
    title = models.CharField(max_length = 200)

