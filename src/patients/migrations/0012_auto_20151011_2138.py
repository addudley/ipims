# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20151011_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='description',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='medicalbackgroundchoice',
            name='description',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='patient',
            name='abdominal_pain_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Abdominal pain', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='consipation_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Constipation', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='headache_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Headache', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='health_insurance_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='health_insurance_provider',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insomnia_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Insomnia', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lack_of_appetite_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Lack of appetite', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nausea_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Nausea', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleepiness_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Sleepiness', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sore_throat_level',
            field=models.CharField(max_length=1, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Sore throat', default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ssn',
            field=models.CharField(max_length=11),
        ),
    ]
