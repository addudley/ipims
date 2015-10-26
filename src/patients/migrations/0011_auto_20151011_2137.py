# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_auto_20151011_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='description',
            field=models.IntegerField(max_length=128),
        ),
        migrations.AlterField(
            model_name='medicalbackgroundchoice',
            name='description',
            field=models.IntegerField(max_length=128),
        ),
        migrations.AlterField(
            model_name='patient',
            name='abdominal_pain_level',
            field=models.IntegerField(verbose_name='Abdominal pain', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.IntegerField(max_length=128),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.IntegerField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='consipation_level',
            field=models.IntegerField(verbose_name='Constipation', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='health_insurance_id',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='health_insurance_provider',
            field=models.IntegerField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insomnia_level',
            field=models.IntegerField(verbose_name='Insomnia', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lack_of_appetite_level',
            field=models.IntegerField(verbose_name='Lack of appetite', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleepiness_level',
            field=models.IntegerField(verbose_name='Sleepiness', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sore_throat_level',
            field=models.IntegerField(verbose_name='Sore throat', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ssn',
            field=models.IntegerField(max_length=11),
        ),
    ]
