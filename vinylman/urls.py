from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin



urlpatterns = [
    # Examples:
    # url(r'^$', 'vinylman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('vinyl.urls')),
]

# Tylko gdy, serwer deveoperski
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )