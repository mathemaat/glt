# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class HNode(models.Model):
  description = models.CharField(max_length=128)
  vleft = models.IntegerField(default=0)
  vright = models.IntegerField(default=0)

  def __str__(self):
    return self.description

  def isRoot(self):
    return self.vleft == 1

  def isLeaf(self):
    return self.vleft + 1 == self.vright

  def getAllParents(self):
    query = ('SELECT p.* '
             'FROM hnodes_hnode c '
             'INNER JOIN hnodes_hnode p ON c.vleft BETWEEN p.vleft AND p.vright '
             'WHERE c.id = %(id)s '
             'ORDER BY p.vleft')
    params = { 'id': int(self.id) }
    return HNode.objects.raw(query, params)

  def getHTMLClass(self):
    if (self.isRoot()):
      return 'root'
    elif (self.isLeaf()):
      return 'leaf'
    else:
      return 'node'

