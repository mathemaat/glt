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

