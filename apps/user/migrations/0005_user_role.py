# Generated by Django 4.2.4 on 2023-09-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_aim'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=10),
        ),
    ]
