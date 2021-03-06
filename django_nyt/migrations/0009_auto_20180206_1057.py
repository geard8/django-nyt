# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-02-06 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_nyt', '0008_auto_20161023_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='activity',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='notification activity'),
        ),
        migrations.AddField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='notification',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='trigged_by_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nyt_notifications_trigged', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
