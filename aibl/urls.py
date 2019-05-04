from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^executive/', include('executive.urls')),
    url(r'^about/$', views.about, name = "about"),
    url(r'^t&c/$', views.terms, name = "terms"),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^send_push/$', views.send_push),
    url(r'^webpush/', include('webpush.urls')),
    url(r'^base_layout.html/$', views.manifest, name = "manifest"),
    url(r'^sw.js/$', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
