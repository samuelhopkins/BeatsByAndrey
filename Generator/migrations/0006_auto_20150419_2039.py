# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0005_auto_20150417_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='lyrics_file',
        ),
        migrations.AlterField(
            model_name='artist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 20, 39, 27, 616575)),
            preserve_default=True,
        ),
    ]
