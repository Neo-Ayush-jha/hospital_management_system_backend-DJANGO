# Generated by Django 4.1.5 on 2023-04-07 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0008_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
    ]
