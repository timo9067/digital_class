from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.user_list, name="user-list"),
    path("profile/", views.user_profile_view, name="user-detail"),
    path("register/", views.user_profile_view, name="user-register"),

]
