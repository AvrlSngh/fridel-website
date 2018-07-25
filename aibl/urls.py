from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^executive/', include('executive.urls')),
    url(r'^about/$', views.about, name = "about"),
    url(r'^t&c/$', views.terms, name = "terms"),
    url(r'^$', views.homepage, name="homepage"),
]

urlpatterns += staticfiles_urlpatterns()
