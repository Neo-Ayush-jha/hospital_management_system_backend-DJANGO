# Generated by Django 4.1.5 on 2023-07-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
