# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 06:33
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(blank=True, max_length=200, null=True, verbose_name='内容')),
                ('version', models.CharField(blank=True, max_length=20, null=True, verbose_name='使用版本')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('reminder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remind_messages', to=settings.AUTH_USER_MODEL, verbose_name='重点提醒人')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='write_messages', to=settings.AUTH_USER_MODEL, verbose_name='发布人')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Message',
            },
        ),
    ]
