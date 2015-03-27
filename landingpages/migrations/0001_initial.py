# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitetools.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Landing page name', max_length=250, verbose_name='Name')),
                ('url', models.CharField(help_text='Landing page URL', max_length=250, verbose_name='URL')),
                ('title', models.CharField(help_text='SEO Title for this page', max_length=250, verbose_name='Title')),
                ('desc', models.TextField(help_text='SEO Description', verbose_name='Description')),
                ('keywords', models.CharField(help_text='SEO Keywords', max_length=250, verbose_name='Keywords')),
                ('language', sitetools.models.fields.LanguageField(help_text='Language this page is intended for', max_length=2, verbose_name='Language', choices=[(b'es', b'Spanish'), (b'en', b'English')])),
                ('content', sitetools.models.fields.HTMLField(help_text='Landing page contents', verbose_name='Content')),
                ('extrahead', models.TextField(help_text='Extra head content (Scripts, meta, etc.)', null=True, verbose_name='Extra head', blank=True)),
                ('template', models.CharField(default=b'landingpages/default.html', help_text='Template name to be used with this landing page', max_length=50, verbose_name='Template')),
            ],
            options={
                'verbose_name': 'Landing Page',
                'verbose_name_plural': 'Landing Pages',
            },
        ),
    ]
