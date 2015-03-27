#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Landing pages models module
===============================================

.. module:: landingpages.models
    :platform: Django
    :synopsis: Landing pages models module
.. moduleauthor:: (C) 2015 Oliver Gutiérrez
"""
# Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Site tools imports
from sitetools.models.fields import LanguageField, HTMLField

class LandingPage(models.Model):
	"""
	Landing Page model class

	"""

	class Meta:
		"""
		Metadata for this model
		"""
		verbose_name=_('Landing Page')
		verbose_name_plural=_('Landing Pages')

	# Fields
	name=models.CharField(_('Name'),max_length=250,
		help_text=_('Landing page name'))
	url=models.CharField(_('URL'),max_length=250,unique=True,
		help_text=_('Landing page URL'))
	active=models.BooleanField(_('Active'),default=True,
		help_text=_('This landing page is currently active'))
	title=models.CharField(_('Title'),max_length=250,
		help_text=_('SEO Title for this page'))
	desc=models.TextField(_('Description'),
		help_text=_('SEO Description'))
	keywords=models.CharField(_('Keywords'),max_length=250,
		help_text=_('SEO Keywords'))
	language=LanguageField(_('Language'),
		help_text=_('Language this page is intended for'))
	content=HTMLField(_('Content'),
		help_text=_('Landing page contents'))
	extrahead=models.TextField(_('Extra head'),blank=True,null=True,
		help_text=_('Extra head content (Scripts, meta, etc.)'))
	template=models.CharField(_('Template'),max_length=50,default='landingpages/default.html',
		help_text=_('Template name to be used with this landing page'))

	# Methods
	def __unicode__(self):
		"""
		Return model unicode representation
		"""
		return self.name
