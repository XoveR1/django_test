from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^blogs/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^signup/$', 'blog.views.signup'),
    url(r'^signup_process/$', 'blog.views.signup_process'),
)
