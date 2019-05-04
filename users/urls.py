from django.contrib import admin
from django.conf.urls import url, include
from users import views
from executive import views as exec_views

app_name = "users"

urlpatterns = [
    url(r'^$', views.normal_user, name = "normal_user"),
    url(r'^order/$', exec_views.get_pickupdrop, name = "pickupdrop"),
    url(r'^delivery_details/$', exec_views.delivery_details, name = "delivery_details"),
    url(r'^final_confirmation/$', exec_views.final_confirmation, name = "final_confirmation"),
    url(r'^order_cancel/$', exec_views.order_cancel, name = "order_cancel"),
    url(r'^orders_history/$', views.orders_history, name = "orders_history"),
    url(r'^other_tasks/$', views.other_task, name = "other_tasks"),
]
