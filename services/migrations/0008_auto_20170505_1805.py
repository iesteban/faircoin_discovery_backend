# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20161112_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.Category'),
            preserve_default=False,
        ),
    ]