# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(default='null', max_length=20),
        ),
    ]
