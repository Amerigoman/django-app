from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_location/$', views.post_location, name='post_location')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
