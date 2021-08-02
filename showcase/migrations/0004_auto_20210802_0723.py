# Generated by Django 3.2.5 on 2021-08-02 07:23

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_alter_glider_gliderimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glider',
            name='size',
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(max_length=1)),
                ('size', models.CharField(max_length=10)),
                ('takeoffWeightMin', models.PositiveIntegerField()),
                ('takeoffWeightMax', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(models.PositiveIntegerField(), message='value is less than min take off weight')])),
                ('gliderWeight', models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('flatArea', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('projectArea', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('cells', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('glider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.glider')),
            ],
        ),
    ]
