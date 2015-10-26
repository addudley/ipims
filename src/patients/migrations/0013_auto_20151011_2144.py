# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20151011_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='consipation_level',
            new_name='constipation_level',
        ),
    ]
