# Generated by Django 4.2.7 on 2024-08-29 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='data',
            new_name='date',
        ),
    ]
