# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='resolved',
            new_name='status',
        ),
        migrations.AddField(
            model_name='record',
            name='doctor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
            preserve_default=False,
        ),
    ]
