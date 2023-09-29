from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    title = models.CharField(max_length=100, null=True, blank=True, 
                             help_text='Your profession')
    bio = models.TextField(default='', blank=True, )

class Teacher(models.Model):
    user_id = models.ForeignKey("user.User", on_delete=models.SET_DEFAULT, default="Unknown")

    def __str__(self) -> str:
        return f"{self.user_id.first_name} {self.user_id.last_name}"