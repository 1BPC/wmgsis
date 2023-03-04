from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("health/", views.health, name="health"),
    path("demographic/", views.demographic, name="demographic"),
    path("manage/", views.manage, name="manage"), 
    path("register/", views.register, name="register"),
    path("satisfaction/", views.satisfaction, name="satisfaction"),
    path("success/", views.success, name="success"),
    path("delete/<id>/", views.delete_graduate, name="delete_graduate"),
    # auth 
    path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html/"), name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
