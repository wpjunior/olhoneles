# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-26 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montanha', '0003_auto_20171024_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biggestsupplierforyear',
            name='year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='collectionrun',
            name='date',
            field=models.DateField(db_index=True, verbose_name='Collection date'),
        ),
        migrations.AlterField(
            model_name='legislature',
            name='date_end',
            field=models.DateField(blank=True, db_index=True, help_text='Date in which this legislature ended.', null=True, verbose_name='Date ended'),
        ),
        migrations.AlterField(
            model_name='legislature',
            name='date_start',
            field=models.DateField(db_index=True, help_text='Date in which this legislature started.', verbose_name='Date started'),
        ),
        migrations.AlterField(
            model_name='mandate',
            name='date_end',
            field=models.DateField(blank=True, db_index=True, help_text='Date in which this mandate ended, paused for taking an executive-branch office, or affiliation change.', null=True, verbose_name='Date ended'),
        ),
        migrations.AlterField(
            model_name='mandate',
            name='date_start',
            field=models.DateField(db_index=True, help_text='Date in which this mandate started; may also be a resumption of a mandate that was paused for taking an executive-branch office, or a party change.', verbose_name='Date started'),
        ),
        migrations.AlterField(
            model_name='perlegislator',
            name='date_end',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='perlegislator',
            name='date_start',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='pernaturebymonth',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]