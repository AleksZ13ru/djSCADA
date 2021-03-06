# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveRTU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_value', models.DateTimeField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceRTU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.IntegerField()),
                ('reg', models.IntegerField()),
                ('type', models.CharField(max_length=8)),
                ('base', models.IntegerField()),
                ('enable_online', models.BooleanField()),
                ('enable_archive', models.BooleanField()),
                ('interval_online', models.IntegerField()),
                ('interval_archive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OnlineRTU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('device_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scada.DeviceRTU')),
            ],
        ),
        migrations.AddField(
            model_name='archivertu',
            name='device_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scada.DeviceRTU'),
        ),
    ]
