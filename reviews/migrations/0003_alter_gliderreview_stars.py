# Generated by Django 3.2.5 on 2021-09-16 17:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210809_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gliderreview',
            name='stars',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
