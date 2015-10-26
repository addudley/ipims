# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20151011_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/', null=True, blank=True),
        ),
    ]
