# -*- coding: utf-8 -*-
"""
URLs for blogging_for_humans.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="blogging_for_humans/base.html")),
]
