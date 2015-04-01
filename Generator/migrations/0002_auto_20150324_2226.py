# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='strength_one',
            new_name='lyric_list',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='strength_three',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='strength_two',
        ),
    ]
