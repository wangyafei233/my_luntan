# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-02 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdemo', '0007_auto_20160902_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='QuestionBody',
            field=models.TextField(max_length=8000, verbose_name='QuestionBody'),
        ),
    ]
