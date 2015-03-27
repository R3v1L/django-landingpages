# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='active',
            field=models.BooleanField(default=True, help_text='This landing page is currently active', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='url',
            field=models.CharField(help_text='Landing page URL', unique=True, max_length=250, verbose_name='URL'),
        ),
    ]
