# Generated by Django 4.2.4 on 2023-09-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('', ''), ('student', 'student'), ('teacher', 'teacher')], default=None, max_length=10),
        ),
    ]
