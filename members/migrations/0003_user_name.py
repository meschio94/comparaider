# Generated by Django 3.2.5 on 2021-08-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_user_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
