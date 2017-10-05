from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
  # organ-systems
  url(r'^organ-systems/$', views.OrganSystemIndexView.as_view(), name='organ_system_index'),
  # e.g. organs/24/brain
  url(r'^organs/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.OrganDetailView.as_view(), name='organ_detail'),
]

