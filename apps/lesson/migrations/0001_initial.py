# Generated by Django 4.2.4 on 2023-09-29 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0010_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='videos/')),
                ('link', models.URLField(null=True)),
                ('small_prewiew', models.ImageField(height_field=40, upload_to='', width_field=60)),
                ('big_preview', models.ImageField(height_field=80, upload_to='', width_field=120)),
                ('lesson_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to=None)),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('teacher_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.module'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher_id',
            field=models.ManyToManyField(to='user.teacher'),
        ),
    ]
