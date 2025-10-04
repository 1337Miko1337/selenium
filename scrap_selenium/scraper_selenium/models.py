from django.db import models

class Phone(models.Model):
    name = models.CharField()
    color = models.JSONField(null=True, blank=True)
    memory = models.JSONField(null=True, blank=True)
    price = models.CharField()
    photo = models.JSONField(null=True, blank=True)
    code = models.CharField()
    fb = models.CharField()
    characteristics = models.JSONField(null=True, blank=True)

