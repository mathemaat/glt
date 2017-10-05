# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import generic

from models import Organ, OrganSystem

class OrganSystemIndexView(generic.ListView):
  model = OrganSystem
  template_name = 'articles/organ_system/index.html'

class OrganDetailView(generic.DetailView):
  model = Organ
  template_name = 'articles/organ/detail.html'

