# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_auto_20151011_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='abdominal_pain_level',
            field=models.CharField(blank=True, verbose_name='Abdominal pain', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='consipation_level',
            field=models.CharField(blank=True, verbose_name='Constipation', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='headache_level',
            field=models.IntegerField(blank=True, verbose_name='Headache', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insomnia_level',
            field=models.CharField(blank=True, verbose_name='Insomnia', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lack_of_appetite_level',
            field=models.CharField(blank=True, verbose_name='Lack of appetite', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nausea_level',
            field=models.IntegerField(blank=True, verbose_name='Nausea', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleepiness_level',
            field=models.CharField(blank=True, verbose_name='Sleepiness', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sore_throat_level',
            field=models.CharField(blank=True, verbose_name='Sore throat', default=0, max_length=1, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
