# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Field, Organ, OrganSystem, Process, Scope, Topic

# Register your models here.
admin.site.register(Field)
admin.site.register(Organ)
admin.site.register(OrganSystem)
admin.site.register(Process)
admin.site.register(Scope)
admin.site.register(Topic)

