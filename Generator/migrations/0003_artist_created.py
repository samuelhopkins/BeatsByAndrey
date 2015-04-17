# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0002_auto_20150324_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 18, 53, 39, 505479)),
            preserve_default=True,
        ),
    ]
