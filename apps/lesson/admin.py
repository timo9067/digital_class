from django.contrib import admin


from . import models


class CustomModuleAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    
class CustomLessonAdmin(admin.ModelAdmin):
    exclude = ("slug",)

admin.site.register(models.Module, CustomModuleAdmin)
admin.site.register(models.Lesson, CustomLessonAdmin)
admin.site.register(models.Video)
# admin.site.register(models.Presentation)


