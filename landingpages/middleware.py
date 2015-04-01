#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Landing pages middleware module
===============================================

.. module:: landingpages.middleware
    :platform: Django
    :synopsis: Landing pages middleware module
.. moduleauthor:: (C) 2015 Oliver Gutiérrez
"""

# Django imports
from django.template.response import TemplateResponse
from django.utils import translation

# Application imports
from landingpages.models import LandingPage

class LandingPagesMiddleware(object):
    """
    Landing pages middleware class
    """
    def process_request(self, request):
        """
        View processing
        """
        try:
            # Search for a landing page with request path to show it if exists
            path=request.path[-1]
            if path != '/':
                path+='/'
            page=LandingPage.objects.get(url=request.path)
            if request.path[-1] != '/':
                return redirect(path)
            else:
                translation.activate(page.language)
                return TemplateResponse(request,page.template,{'page': page})
        except:
            return None
        

