# Generated by Django 4.2 on 2023-04-27 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_userdata_os_remove_userdata_browser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='all_lang',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='cords',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='display',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='lang',
        ),
    ]
