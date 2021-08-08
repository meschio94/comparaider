import os
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.urls import reverse
from members.models import User
import django.utils.timezone as timezone

import showcase.fields


def get_upload_glider_image(instance, filename):
    return '{0}/{1}/{2}/{3}/{4}'.format("products", instance.maker, instance.year, instance.name, instance.name,
                                        filename)


def get_upload_maker_logo_image(instance, filename):
    return '{0}/{1}/{2}/{3}'.format("products", instance.name, instance.name, "logo", filename)


class Maker(models.Model):
    name = models.CharField(max_length=255)
    logoImage = models.ImageField(default=None, upload_to=get_upload_maker_logo_image)
    textIntro = models.TextField(blank=True, null=True)
    account = models.OneToOneField(User, related_name='manufacturer_user', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('showcase:manufacture_profile', kwargs={'pk': self.pk})


class Glider(models.Model):
    name = models.CharField(max_length=255)
    maker = models.ForeignKey(Maker, related_name='manufacturer_glider', on_delete=models.CASCADE)
    year = showcase.fields.Year(max_value=timezone.now().year, default=timezone.now().year)
    gliderImage = models.ImageField(upload_to=get_upload_glider_image, default=None)

    def __str__(self):
        return f"{self.maker} - {self.name}"


CERTIFICATION_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]


class Size(models.Model):
    glider = models.ForeignKey(Glider, related_name='glider_size', on_delete=models.CASCADE)
    certification = models.CharField(max_length=1, choices=CERTIFICATION_CHOICES)  # input selezionatore
    size = models.CharField(max_length=10)
    takeoffWeightMin = models.PositiveIntegerField()
    takeoffWeightMax = models.PositiveIntegerField()
    gliderWeight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    flatArea = models.PositiveIntegerField()
    projectArea = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    cells = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.glider.name} : {self.size}"


class GliderReview(models.Model):
    glider = models.ForeignKey(Glider, on_delete=models.CASCADE, related_name='glider_review')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
