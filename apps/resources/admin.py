from django.contrib import admin
from apps.resources import models

# Register your models here.


class CustomResources(admin.ModelAdmin):
    list_display = [
        "username",
        "user_title",
        "title",
        "description",
    ]


admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.Review)
admin.site.register(models.ResourcesTag)
admin.site.register(models.Rating)
