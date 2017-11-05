# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import generic

from models import HNode

class HNodeListView(generic.ListView):
  model = HNode
  template_name = 'hnodes/full-tree.html'

class HNodeDetailView(generic.DetailView):
  model = HNode
  template_name = 'hnodes/detail.html'

