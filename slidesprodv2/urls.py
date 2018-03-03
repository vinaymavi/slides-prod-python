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
    url(r'^api-root/', views.api_root, name="api_root"),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^question-set/(?P<pk>[0-9]+)$', views.QuerySetDetail.as_view(),name="questionset-detail"),
    url(r'^question-set/questions/(?P<pk>[0-9]+)$', views.QuestionsList.as_view(),name="question-list"),
    url(r'^question-set/', views.QuestionSetList.as_view(),name="question_set-list"),
    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
)

if settings.DEBUG:
    urlpatterns += tuple(static(settings.STATIC_URL, view=serve, show_indexes=True))
