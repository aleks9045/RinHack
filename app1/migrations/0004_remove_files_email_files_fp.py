# Generated by Django 4.2 on 2023-04-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_user_files_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='email',
        ),
        migrations.AddField(
            model_name='files',
            name='fp',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
