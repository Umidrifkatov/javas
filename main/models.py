from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=60, blank=True, default=None, null=True)
    phone = models.CharField(max_length=18)
    mail = models.CharField(max_length=100, blank=True, default=None, null=True)
    comment = models.TextField(max_length=500, blank=True, default=None, null=True)
