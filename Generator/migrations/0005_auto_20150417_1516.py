# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0004_auto_20150417_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 15, 16, 28, 535437)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='lyrics_file',
            field=models.FileField(upload_to=b'artists'),
            preserve_default=True,
        ),
    ]
