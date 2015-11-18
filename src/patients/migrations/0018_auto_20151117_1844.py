# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20151026_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='abdominal_pain_level',
            field=models.CharField(max_length=2, verbose_name='Abdominal pain', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='constipation_level',
            field=models.CharField(max_length=2, verbose_name='Constipation', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='headache_level',
            field=models.CharField(max_length=2, verbose_name='Headache', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insomnia_level',
            field=models.CharField(max_length=2, verbose_name='Insomnia', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lack_of_appetite_level',
            field=models.CharField(max_length=2, verbose_name='Lack of appetite', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nausea_level',
            field=models.CharField(max_length=2, verbose_name='Nausea', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleepiness_level',
            field=models.CharField(max_length=2, verbose_name='Sleepiness', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sore_throat_level',
            field=models.CharField(max_length=2, verbose_name='Sore throat', default=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
    ]
