# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsc', '0003_auto_20171012_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsc',
            name='tsc_type',
            field=models.IntegerField(choices=[(2, 'Small Clusters'), (1, 'Large Clusters')], verbose_name='集群类型'),
        ),
    ]
