# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connection
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from models import HNode

class HNodeListView(generic.ListView):
  model = HNode
  template_name = 'hnodes/full-tree.html'

class HNodeDetailView(generic.DetailView):
  model = HNode
  template_name = 'hnodes/detail.html'

def insertChild(request, pk, slug):
  hnode = get_object_or_404(HNode, pk=pk)

  with connection.cursor() as cursor:
    query = ('UPDATE hnodes_hnode '
             'SET vleft = vleft + 2 '
             'WHERE vleft >= %(vright)s')
    cursor.execute(query, {'vright': hnode.vright})

    query = ('UPDATE hnodes_hnode '
             'SET vright = vright + 2 '
             'WHERE vright >= %(vright)s')
    cursor.execute(query, {'vright': hnode.vright})

  new = HNode()
  new.description = request.POST['description']
  new.vleft = hnode.vright
  new.vright = hnode.vright + 1
  new.save();

  return HttpResponseRedirect(reverse('hnodes:detail', args=(new.id, 'todo')))

