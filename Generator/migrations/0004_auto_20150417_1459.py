# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0003_artist_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='lyrics_file',
            field=models.FileField(default=b'/foo', storage=django.core.files.storage.FileSystemStorage(location=b'static/Generator/lyrics'), upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 14, 59, 54, 287975)),
            preserve_default=True,
        ),
    ]
