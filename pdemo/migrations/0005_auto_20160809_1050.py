# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdemo', '0004_auto_20160809_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='QuestionTime',
            field=models.DateTimeField(auto_now=True, verbose_name='QuestionTime'),
        ),
    ]
