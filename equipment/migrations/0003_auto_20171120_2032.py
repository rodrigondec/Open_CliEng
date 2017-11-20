# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_auto_20171120_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='equipment',
        ),
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Maintenance',
        ),
    ]