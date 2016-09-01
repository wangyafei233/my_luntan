#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from django import template
# from django.conf import settings
# import json
# register = template.Library()
#
# # list all columns
# PROJECTS_COLUMNS_DATA = getattr(settings, 'PROJECTS_COLUMNS_DATA', [])
#
#
# @register.inclusion_tag('chart/action_tags.html')
# def pie_chart_action(action_data):
#     """
#     :param chart_data:
#     :return:
#     """
#     data = None
#     if action_data:
#         data = json.dumps(action_data)
#     return {"data_items": data, "data": action_data}
