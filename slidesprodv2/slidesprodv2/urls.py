from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from api import views
import session_csrf


session_csrf.monkeypatch()

from django.contrib import admin

admin.autodiscover()

urlpatterns = (
    # Examples:
    url(r'^$', views.index, name='home'),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^api/', views.api),
    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
)

if settings.DEBUG:
    urlpatterns += tuple(static(settings.STATIC_URL, view=serve, show_indexes=True))
