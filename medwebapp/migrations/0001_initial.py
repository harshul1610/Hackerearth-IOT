# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 12:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='klopvalues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klopid', models.CharField(max_length=10)),
                ('heart_rate', models.IntegerField(default=0)),
                ('resp_rate', models.IntegerField(default=0)),
                ('blood_pressure_sys', models.IntegerField(default=0)),
                ('blood_pressure_dia', models.IntegerField(default=0)),
                ('sugar_level', models.IntegerField(default=0)),
                ('spo2_content', models.IntegerField(default=0)),
                ('ECG_pattern', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('klopid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=22)),
                ('sg', models.CharField(max_length=3)),
                ('bp', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('klopid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=22)),
                ('sg', models.CharField(max_length=3)),
                ('bp', models.CharField(max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
