# Generated by Django 4.1.5 on 2023-03-21 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabilauthorised',
            name='cableNumber',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.cabil'),
        ),
    ]
