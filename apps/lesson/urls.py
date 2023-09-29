from django.urls import path
from . import views

urlpatterns = [
    path("<slug:topic_slug>/<int:lesson_id>/<slug:lesson_slug>/", views.lesson_detail_view, name="lesson-detail"),
    path("<slug:topic_slug>/", views.lesson_list_view, name="lesson-list"),
    path("", views.home_page_view, name="home-page"),
]
