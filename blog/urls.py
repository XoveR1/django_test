from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /blog/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /blog/edit/5/
    url(r'^edit/(?P<pk>\d+)/$', views.EditView.as_view(), name='edit'),
    # ex: /blog/save/5/
    url(r'^save/(?P<blog_id>\d+)/$', views.blog_save, name='save'),
)