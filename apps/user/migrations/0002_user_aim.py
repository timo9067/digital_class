# Generated by Django 4.2.4 on 2023-08-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aim',
            field=models.TextField(default=''),
        ),
    ]
