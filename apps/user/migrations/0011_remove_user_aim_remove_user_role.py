# Generated by Django 4.2.4 on 2023-09-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aim',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]