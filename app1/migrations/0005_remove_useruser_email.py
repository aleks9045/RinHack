# Generated by Django 4.2 on 2023-04-28 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_files_email_files_fp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useruser',
            name='email',
        ),
    ]
