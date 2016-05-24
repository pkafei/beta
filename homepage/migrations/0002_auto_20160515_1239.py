# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Social_Media',
        ),
        migrations.AddField(
            model_name='landing_page',
            name='social_media_icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='landing_page',
            name='social_media_icon_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
