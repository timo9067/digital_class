from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Module(models.Model):
    teacher_id = models.ForeignKey("user.Teacher", null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, blank=False)
    logo = models.ImageField()
    description = models.TextField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Module, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    module_id = models.ForeignKey("Module", on_delete=models.CASCADE)
    teacher_id = models.ManyToManyField("user.Teacher")
    topic = models.CharField(max_length=100, null=False)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic)
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.module_id} - {self.topic}"

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    lesson_id = models.ForeignKey("Lesson", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Presentation(models.Model):
    topic = models.CharField(max_length=50, null=False)
    file = models.FileField(upload_to=None, max_length=100)
    lesson_id = models.ForeignKey("Lesson", on_delete=models.CASCADE)
