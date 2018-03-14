from django.conf.urls import url, include

from django.contrib import admin
from collection import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
