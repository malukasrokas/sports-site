# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 12:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0008_auto_20170418_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='awayTeamScore',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='homeTeamScore',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='newsfeed.Team'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]