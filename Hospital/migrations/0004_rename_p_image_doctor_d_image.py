# Generated by Django 4.1.5 on 2023-03-06 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_alter_patient_room_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='p_image',
            new_name='d_image',
        ),
    ]
