# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField


class Risk(models.Model):
    label = models.CharField(null=False, blank=False, max_length=20)
    description = models.CharField(null=True, max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    value = JSONField(null=True, blank=True)

    class Meta:
        ordering = ('date_created',)