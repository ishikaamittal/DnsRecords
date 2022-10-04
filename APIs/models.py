from django.db import models

# Create your models here.
class DnsRecords(models.Model):
    domain =  models.CharField(max_length=50)
    ip = models.CharField(max_length=16)

    def __str__(self):
        return self.domain 