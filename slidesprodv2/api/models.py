from __future__ import unicode_literals

from django.db import models

class Greetings(models.Model):
    number = models.IntegerField(max_length=100)
    messaage = models.TextField(max_length=200)

