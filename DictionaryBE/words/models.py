from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    word = models.CharField(max_length=255)
    base = models.CharField(max_length=255)
    encoding = models.CharField(max_length=255)

    class Meta:
        db_table = 'words'
        app_label = 'words'


class Sentence(models.Model):
    sentence = models.CharField(max_length=255)
    words = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    class Meta:
        db_table = 'sentences'
        app_label = 'words'
        unique_together = (('sentence', 'token'),)
