from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255)
    base = models.CharField(max_length=255)
    encoding = models.CharField(max_length=255)
