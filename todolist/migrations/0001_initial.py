# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskText', models.CharField(max_length=300)),
                ('startDate', models.DateTimeField()),
                ('deadLineDate', models.DateTimeField()),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
    ]
