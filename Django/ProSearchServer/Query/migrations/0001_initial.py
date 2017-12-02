# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20)),
                ('query', models.TextField(default=b'This is default query', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('name', models.TextField()),
                ('q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Query.Query')),
            ],
        ),
    ]
