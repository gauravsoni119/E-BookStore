# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 11:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160206_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
