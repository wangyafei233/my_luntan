# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-02 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdemo', '0003_bbs_questiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='QuestionType',
            field=models.CharField(blank=True, max_length=255, verbose_name='QuestionType'),
        ),
    ]