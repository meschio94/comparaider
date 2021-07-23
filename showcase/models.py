from django.db import models

import showcase.fields
import django.utils.timezone as timezone


class Maker(models.Model):
    name = models.CharField(max_length=255)


class Glider(models.Model):
    name = models.CharField(max_length=255)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    year = showcase.fields.Year(max_value=timezone.now().year)
    gliderWeight = models.DecimalField(max_digits=10, decimal_places=2)
