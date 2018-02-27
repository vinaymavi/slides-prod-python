from __future__ import unicode_literals

from django.db import models

class Greeting(models.Model):
    number = models.IntegerField(max_length=100)
    messaage = models.TextField(max_length=200)

    def __str__(self):
        return self.messaage
