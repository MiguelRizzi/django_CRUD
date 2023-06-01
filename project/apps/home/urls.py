from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/index.html"), name="index"),
    path("info/", TemplateView.as_view(template_name="home/info.html"), name="info"),
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("register/", views.register, name="register")
]
