# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-15 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='language',
            field=models.IntegerField(choices=[(1, 'python'), (2, 'java'), (3, 'php'), (4, 'javascript'), (5, 'C++'), (6, 'assembly'), (7, 'ruby'), (8, 'perl'), (9, 'shell')], default=1, max_length=100),
        ),
    ]
