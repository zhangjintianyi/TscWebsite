# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsc', '0011_auto_20171021_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsc',
            name='tsc_type',
            field=models.IntegerField(choices=[(1, 'Large Clusters'), (2, 'Small Clusters')], verbose_name='集群类型'),
        ),
    ]