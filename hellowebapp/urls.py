from django.conf.urls import patterns, include, url

from django.contrib import admin
from collection import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='home')
    url(r'^admin/', include(admin.site.urls)),
)
