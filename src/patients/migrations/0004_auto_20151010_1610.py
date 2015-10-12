# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20151010_1606'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicalBackgroundChoices',
            new_name='MedicalBackgroundChoice',
        ),
    ]
