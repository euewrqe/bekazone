# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-31 10:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Another',
        ),
    ]