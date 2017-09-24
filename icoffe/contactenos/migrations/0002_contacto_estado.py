# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-24 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactenos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Recibido'), (2, 'En proceso'), (3, 'Resuelto')], default=1),
        ),
    ]