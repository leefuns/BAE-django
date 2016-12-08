# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('img', models.ImageField(default=b'uploads/default.jpg', upload_to=b'uploads/%Y-%m-%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('author', models.CharField(default=b'Lee', max_length=10, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('desc', models.CharField(max_length=255, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('publish_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='MetaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('web_keywords', models.CharField(max_length=150, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('web_description', models.CharField(max_length=200, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u4fe1\u606f',
            },
        ),
    ]
