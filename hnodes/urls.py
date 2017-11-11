from django.conf.urls import url

from . import views

app_name = 'hnodes'
urlpatterns = [
  # e.g. 15/tissue
  url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.HNodeDetailView.as_view(), name='detail'),
  # e.g. 15/tissue/insert-child
  url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/insert-child/$', views.insertChild, name='insert-child'),
  # e.g. 15/tissue/insert-sibling-left
  url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/insert-sibling-left/$',  views.insertSiblingLeft,  name='insert-sibling-left'),
  # e.g. 15/tissue/insert-sibling-right
  url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/insert-sibling-right/$', views.insertSiblingRight, name='insert-sibling-right'),
  # e.g. 15/tissue/delete
  url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/delete/$', views.delete, name='delete'),
  # e.g. node-tree
  url(r'^full-tree/$', views.HNodeListView.as_view(), name='full-tree'),
]

