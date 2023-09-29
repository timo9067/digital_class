from django.contrib import admin
from apps.user import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.


# class CustomUser(UserAdmin):
#     fieldsets =  UserAdmin.fieldsets + (("Additional Info", {"fields": ("title", "bio")}),)

class CustomUser(UserAdmin):
    # Define the fieldsets you want to include
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Additional Info', {'fields': ('title', 'bio')}),
    )
    
    # Remove the "Groups" and "User permissions" sections
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

admin.site.register(models.User, CustomUser)
admin.site.register(models.Teacher)
