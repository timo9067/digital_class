# Generated by Django 4.2.4 on 2023-09-06 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resources',
            options={'verbose_name_plural': 'Resourses'},
        ),
        migrations.RemoveField(
            model_name='resources',
            name='rate',
        ),
    ]