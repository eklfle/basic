from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login_try/", views.login_try, name="login_try"),

]