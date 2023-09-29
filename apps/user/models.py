from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USER_ROLE = (
    ("",""),
    ("student", "student"),
    ("teacher", "teacher"),
)

class User(AbstractUser):
    title = models.CharField(max_length=100, null=True, blank=True, 
                             help_text='Your profession')
    bio = models.TextField(default='', blank=True, )
    aim = models.TextField(default='', blank=True, )
    role = models.CharField(max_length=10, choices=USER_ROLE, default=None,)

