# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import generic

from models import Field, Organ, OrganSystem, Topic

class FieldIndexView(generic.ListView):
  model = Field
  template_name = 'articles/field/index.html'

class OrganSystemIndexView(generic.ListView):
  model = OrganSystem
  template_name = 'articles/organ_system/index.html'

class TopicIndexView(generic.ListView):
  model = Topic
  template_name = 'articles/topic/index.html'

class OrganDetailView(generic.DetailView):
  model = Organ
  template_name = 'articles/organ/detail.html'

