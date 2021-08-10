# Generated by Django 3.2.5 on 2021-08-09 08:59

from django.db import migrations, models
import django.db.models.deletion
import showcase.models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glider',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer_glider', to='showcase.maker'),
        ),
        migrations.AlterField(
            model_name='maker',
            name='logoImage',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=showcase.models.get_upload_maker_logo_image),
        ),
        migrations.DeleteModel(
            name='GliderReview',
        ),
    ]