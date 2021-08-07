# Generated by Django 3.2.5 on 2021-08-07 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='members.user')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_person',
            field=models.BooleanField(default=True),
        ),
    ]