# Generated by Django 4.1.5 on 2023-07-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_post',
            field=models.CharField(choices=[('nurse', 'nurse'), ('receptionists', 'receptionists'), ('pherma_staff', 'pherma_staff'), ('pathology_staff', 'pathology_staff'), ('clerk', 'clerk')], max_length=20),
        ),
    ]