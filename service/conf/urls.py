'''
Service urls main configuration.
'''

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^api/twitter/', include('twitter.urls', namespace='twitter')),
    # url(r'^api/auth/', include('rest_framework.urls', namespace="api-auth")),
    url(r'^admin/', admin.site.urls),
]
