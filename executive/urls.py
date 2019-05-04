from django.contrib import admin
from django.conf.urls import url, include
from executive import views



app_name = "executive"

urlpatterns = [
    url(r'^$', views.executive_user, name = "executive_user"),
    url(r'^confirm/$', views.get_executivelocation, name = "executive_location"),
    url(r'^user_confirmation/$', views.user_confirmation, name = "user_confirmation"),
    # url(r'^other_task_executive/$', views.other_task_executive, name = "other_task_executive"),
    url(r'^(?P<id>[\w-]+)/$', views.order_detail, name="order_detail"),
    url(r'^webpush/', include('webpush.urls')),

    # url(r'^order_completed/$', views.order_completed, name="order_completed"),
]
