# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20151101_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='status',
            new_name='resolved',
        ),
    ]
