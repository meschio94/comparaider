# Generated by Django 3.2.5 on 2021-08-02 09:47

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_auto_20210802_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='cells',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='size',
            name='certification',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1),
        ),
        migrations.AlterField(
            model_name='size',
            name='flatArea',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='size',
            name='glider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glider_size', to='showcase.glider'),
        ),
        migrations.AlterField(
            model_name='size',
            name='gliderWeight',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='size',
            name='projectArea',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='size',
            name='takeoffWeightMax',
            field=models.PositiveIntegerField(),
        ),
    ]
