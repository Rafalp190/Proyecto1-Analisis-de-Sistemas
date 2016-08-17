from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inventario (models.Model):
    id = models.BigIntegerField(primary_key=True)
    content = models.CharField(max_length=255, blank=True)
    date = models.BigIntegerField(blank=True, null=True)
    recipients = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True)
    sender = models.ForeignKey('Emailaccount', blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'email'