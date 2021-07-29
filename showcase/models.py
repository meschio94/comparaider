import os
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

import showcase.fields
import django.utils.timezone as timezone

def get_upload_glider_image(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.maker,instance.year,instance.name,instance.name, filename)

class Maker(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Glider(models.Model):
    name = models.CharField(max_length=255)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    year = showcase.fields.Year(max_value=timezone.now().year, default=timezone.now().year)
    gliderWeight = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    gliderImage = models.ImageField(upload_to= get_upload_glider_image, default=None)

    def __str__(self):
        return f"{self.maker} - {self.name}"


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title



