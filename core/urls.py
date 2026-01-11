from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("run/create/", views.create_run_plan, name="create_run_plan"),
    path("recommendations/", views.recommendation_list, name="recommendation_list"),
]
