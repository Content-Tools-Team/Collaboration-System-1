# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 12:09
from __future__ import unicode_literals

import UserRolesPermission.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRolesPermission', '0007_merge_20180321_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='photo',
            field=models.ImageField(upload_to=UserRolesPermission.helpers.get_file_path),
        ),
    ]
