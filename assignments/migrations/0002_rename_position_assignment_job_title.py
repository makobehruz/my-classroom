# Generated by Django 5.1.6 on 2025-02-14 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='position',
            new_name='job_title',
        ),
    ]
