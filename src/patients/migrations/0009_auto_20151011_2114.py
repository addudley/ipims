# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_auto_20151011_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='abdominal_pain',
            new_name='abdominal_pain_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='consipation',
            new_name='consipation_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='headache',
            new_name='headache_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='insomnia',
            new_name='insomnia_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='lack_of_appetite',
            new_name='lack_of_appetite_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='nausea',
            new_name='nausea_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='tired',
            new_name='sleepiness_level',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='sore_throat',
            new_name='sore_throat_level',
        ),
    ]
