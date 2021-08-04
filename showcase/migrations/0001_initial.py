# Generated by Django 3.2.5 on 2021-08-04 15:13

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import showcase.fields
import showcase.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', showcase.fields.Year(default=2021)),
                ('gliderWeight', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('gliderImage', models.ImageField(default=None, upload_to=showcase.models.get_upload_glider_image)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logoImage', models.ImageField(default=None, upload_to=showcase.models.get_upload_maker_logo_image)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('size', models.CharField(max_length=10)),
                ('takeoffWeightMin', models.PositiveIntegerField()),
                ('takeoffWeightMax', models.PositiveIntegerField()),
                ('gliderWeight', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('flatArea', models.PositiveIntegerField()),
                ('projectArea', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('cells', models.PositiveIntegerField()),
                ('glider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glider_size', to='showcase.glider')),
            ],
        ),
        migrations.AddField(
            model_name='glider',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.maker'),
        ),
    ]
