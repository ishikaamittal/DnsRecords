from django.db import models
import socket
# Create your models here.
class DnsRecords(models.Model):
    domain =  models.CharField(max_length=50)
    ip = models.CharField(max_length=16)

    class Meta:
            verbose_name_plural = "records"

    def __str__(self):
        return self.domain 