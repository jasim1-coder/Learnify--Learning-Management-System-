# Generated by Django 4.2.7 on 2024-08-29 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_alter_profile_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
    ]
