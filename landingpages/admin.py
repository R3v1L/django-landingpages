#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Landing pages administration module
===============================================

.. module:: landingpages.admin
    :platform: Django
    :synopsis: Landing pages administration module
.. moduleauthor:: (C) 2015 Oliver Gutiérrez
"""

# Django imports
from django.contrib import admin

# Site tools imports
from sitetools.admin import BaseModelAdmin

# Application imports
from landingpages.models import LandingPage

class LandingPageAdmin(BaseModelAdmin):
    """
    Landing page administration class
    """
    list_display = ('name','url','language','template',)
    list_filter = ('language','template',)
    search_fields = ('name','title','keywords',)

# Register models
admin.site.register(LandingPage,LandingPageAdmin)