from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("teacher/", include("apps.teacher.urls")),
    path("user/", include("apps.user.urls")),
    path("", include("apps.lesson.urls")),
]
