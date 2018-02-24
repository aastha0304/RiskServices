# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 05:55
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
    ]