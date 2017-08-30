# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Field(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  def __str__(self):
    return self.description

class OrganSystem(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  def __str__(self):
    return self.description

@python_2_unicode_compatible
class Organ(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  organsystem = models.ForeignKey(OrganSystem)

  def __str__(self):
    return self.description

@python_2_unicode_compatible
class Process(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = 'Processes'

@python_2_unicode_compatible
class Scope(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  def __str__(self):
    return self.description

@python_2_unicode_compatible
class Topic(models.Model):
  description = models.CharField(max_length=128)
  token       = models.CharField(max_length=32, editable=False)

  def __str__(self):
    return self.description

