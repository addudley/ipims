# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20151010_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='abdominal_pain',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='consipation',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='headache',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='insomnia',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='lack_of_appetite',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='nausea',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='sore_throat',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='tired',
            field=models.CharField(default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
