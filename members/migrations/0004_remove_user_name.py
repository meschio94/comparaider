# Generated by Django 3.2.5 on 2021-08-10 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
