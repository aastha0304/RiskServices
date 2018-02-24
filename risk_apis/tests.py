# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework import status
from django.test import TestCase, Client
from models import Risk
from serializers import RiskSerializer
from django.urls import reverse
from views import RiskViewSet
from rest_framework.test import APIRequestFactory


# Create your tests here.
class GetAllRisksTest(TestCase):
    """ Test module for GET all risks API """

    def setUp(self):
        Risk.objects.create(label='prize', description='prize insurance',
            value={
                'coverage_limit': '10000',
                'event': 'golf tournament'
        })
        Risk.objects.create(label='accident',
            value={
                'coverage_limit': '10000',
                'vehicle_type': '4_wheeler'
        })
        Risk.objects.create(label='houses',
            value={
                'coverage_limit': '10000',
                'age_of_house_limit': '2'
        })

    def test_get_risk_detail(self):
        factory = APIRequestFactory().get('')
        risk_detail = RiskViewSet.as_view({
            'get': 'retrieve'
        })
        risk = Risk.objects.create(label='accident', description='accident insurance',
            value={
                'coverage_limit': '10000',
                'vehicle': '4 wheeler'
        })
        response = risk_detail(factory, pk=risk.pk)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.content,
                          '{"id":7,"label":"accident","description":"accident insurance","value":{"coverage_limit":"10000","vehicle":"4 wheeler"}}')

    def test_get_all_risks(self):
        factory = APIRequestFactory().get('')
        risk_list = RiskViewSet.as_view({
            'get': 'list'
        })
        response = risk_list(factory)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.content,
                          '[{"id":1,"label":"prize","description":"prize insurance","value":{"coverage_limit":"10000","event":"golf tournament"}},{"id":2,"label":"accident","description":null,"value":{"coverage_limit":"10000","vehicle_type":"4_wheeler"}},{"id":3,"label":"houses","description":null,"value":{"coverage_limit":"10000","age_of_house_limit":"2"}}]')