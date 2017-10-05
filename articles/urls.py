from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
  # e.g. organs/24/brain
  url(r'^organs/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.OrganDetailView.as_view(), name='organ_detail'),
]

