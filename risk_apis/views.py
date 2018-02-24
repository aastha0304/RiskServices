# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from models import Risk
from serializers import RiskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets


class RiskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
