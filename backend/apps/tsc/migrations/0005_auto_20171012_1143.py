# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsc', '0004_auto_20171012_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbs',
            name='dbs_type',
            field=models.IntegerField(choices=[(2, 'Oracle'), (1, 'MySQL')], verbose_name='数据库类型'),
        ),
        migrations.AlterField(
            model_name='tsc',
            name='tsc_type',
            field=models.IntegerField(choices=[(1, 'Large Clusters'), (2, 'Small Clusters')], verbose_name='集群类型'),
        ),
    ]
