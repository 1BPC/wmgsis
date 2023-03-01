from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # path("", include("WMGSIS Assignment.apps.public.urls")),
   # path("accounts/", include("WMGSIS Assignment.apps.accounts.urls")),

    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("health/", views.health, name="health"),
    path("demographic/", views.demographic, name="demographic"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("satisfaction/", views.satisfaction, name="satisfaction"),
    path("success/", views.success, name="success"),
    path("settings/", views.settings, name="settings"),

]
