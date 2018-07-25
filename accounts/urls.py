from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^login/$', views.login_view, name = "login"),
    url(r'^signup/$', views.signup_view.as_view(), name = "signup"),
    url(r'^logout/$', views.logout_view, name = "logout"),
]
