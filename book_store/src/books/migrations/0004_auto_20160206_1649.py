# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160206_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]