from django.urls import path, include
from django.contrib import admin
admin.autodiscover()



# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('' , include('test_10.urls')),
]