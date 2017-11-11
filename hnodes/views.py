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

def insertSiblingLeft(request, pk, slug):
  hnode = get_object_or_404(HNode, pk=pk)

  with connection.cursor() as cursor:
    query = ('UPDATE hnodes_hnode '
             'SET vleft = vleft + 2 '
             'WHERE vleft >= %(vleft)s')
    cursor.execute(query, {'vleft': hnode.vleft})

    query = ('UPDATE hnodes_hnode '
             'SET vright = vright + 2 '
             'WHERE vright >= %(vleft)s')
    cursor.execute(query, {'vleft': hnode.vleft})

  new = HNode()
  new.description = request.POST['description']
  new.vleft = hnode.vleft
  new.vright = hnode.vleft + 1
  new.save();

  return HttpResponseRedirect(reverse('hnodes:detail', args=(new.id, 'todo')))

def insertSiblingRight(request, pk, slug):
  hnode = get_object_or_404(HNode, pk=pk)

  with connection.cursor() as cursor:
    query = ('UPDATE hnodes_hnode '
             'SET vleft = vleft + 2 '
             'WHERE vleft > %(vright)s')
    cursor.execute(query, {'vright': hnode.vright})

    query = ('UPDATE hnodes_hnode '
             'SET vright = vright + 2 '
             'WHERE vright > %(vright)s')
    cursor.execute(query, {'vright': hnode.vright})

  new = HNode()
  new.description = request.POST['description']
  new.vleft = hnode.vright + 1
  new.vright = hnode.vright + 2
  new.save();

  return HttpResponseRedirect(reverse('hnodes:detail', args=(new.id, 'todo')))

def delete(request, pk, slug):
  hnode = get_object_or_404(HNode, pk=pk)

  offset = hnode.vright - hnode.vleft + 1

  with connection.cursor() as cursor:
    query = ('DELETE FROM hnodes_hnode '
             'WHERE vleft > %(vleft)s '
             'AND vright < %(vright)s')
    cursor.execute(query, {'vleft': hnode.vleft, 'vright': hnode.vright})

    query = ('UPDATE hnodes_hnode '
             'SET vleft = vleft - %(offset)s '
             'WHERE vleft > %(vright)s')
    cursor.execute(query, {'offset': offset, 'vright': hnode.vright})

    query = ('UPDATE hnodes_hnode '
             'SET vright = vright - %(offset)s '
             'WHERE vright > %(vright)s')
    cursor.execute(query, {'offset': offset, 'vright': hnode.vright})

  hnode.delete()

  return HttpResponseRedirect(reverse('hnodes:full-tree'))

