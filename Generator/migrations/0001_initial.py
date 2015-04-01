# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, verbose_name=b"Artist's Name", primary_key=True)),
                ('strength_one', models.TextField()),
                ('strength_two', models.TextField()),
                ('strength_three', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
