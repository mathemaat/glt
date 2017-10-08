from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
  # fields
  url(r'^fields/$', views.FieldIndexView.as_view(), name='field_index'),
  # organ-systems
  url(r'^organ-systems/$', views.OrganSystemIndexView.as_view(), name='organ_system_index'),
  # process
  url(r'^processes/$', views.ProcessIndexView.as_view(), name='process_index'),
  # topics
  url(r'^topics/$', views.TopicIndexView.as_view(), name='topic_index'),
  # e.g. organs/24/brain
  url(r'^organs/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.OrganDetailView.as_view(), name='organ_detail'),
]

