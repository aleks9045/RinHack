# Generated by Django 4.2 on 2023-04-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='OS',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='browser',
        ),
        migrations.AddField(
            model_name='userdata',
            name='fp',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
