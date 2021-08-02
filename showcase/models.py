import os
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import django.utils.timezone as timezone

import showcase.fields


def get_upload_glider_image(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.maker,instance.year,instance.name,instance.name, filename)

def get_upload_maker_logo_image(instance, filename):
    return '{0}/{1}/{2}'.format(instance.name, instance.name , "logo" , filename)

class Maker(models.Model):
    name = models.CharField(max_length=255)
    logoImage = models.ImageField(default=None, upload_to= get_upload_maker_logo_image)
    def __str__(self):
        return self.name


class Glider(models.Model):
    name = models.CharField(max_length=255)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    year = showcase.fields.Year(max_value=timezone.now().year, default=timezone.now().year)
    gliderWeight = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))]) #da eliminare
    gliderImage = models.ImageField(upload_to= get_upload_glider_image, default=None)

    def __str__(self):
        return f"{self.maker} - {self.name}"

CERTIFICATION_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]

class Size(models.Model):
    glider = models.ForeignKey(Glider, on_delete=models.CASCADE, related_name='glider_size')
    certification = models.CharField(max_length=1, choices=CERTIFICATION_CHOICES) #input selezionatore
    size = models.CharField(max_length=10)
    takeoffWeightMin = models.PositiveIntegerField()
    takeoffWeightMax = models.PositiveIntegerField()
    gliderWeight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    flatArea = models.PositiveIntegerField()
    projectArea = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    cells = models.PositiveIntegerField()

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title





