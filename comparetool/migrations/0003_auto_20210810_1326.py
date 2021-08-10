# Generated by Django 3.2.5 on 2021-08-10 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_auto_20210809_0859'),
        ('comparetool', '0002_compareitems_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeitem',
            name='compareItems',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size_item', to='comparetool.compareitems'),
        ),
        migrations.AlterField(
            model_name='sizeitem',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size_info', to='showcase.size'),
        ),
    ]
