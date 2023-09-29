from django.urls import path

from . import views


urlpatterns = [
    path("dashboard/", views.teacher_dashboard_view, name="teacher-dashboard"),
    path("students-list/", views.teacher_stud_list_view, name="students-list"),
]
