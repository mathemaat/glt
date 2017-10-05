# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import generic

from models import Organ

class OrganDetailView(generic.DetailView):
  model = Organ
  template_name = 'articles/organ/detail.html'

