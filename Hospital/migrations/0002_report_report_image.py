# Generated by Django 4.1.5 on 2023-03-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_image',
            field=models.ImageField(blank=True, null=True, upload_to='report/'),
        ),
    ]
