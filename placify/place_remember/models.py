from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    comment = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
