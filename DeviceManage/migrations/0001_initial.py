# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-11-06 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=96, null=True, verbose_name='\u4e8c\u7ef4\u7801')),
                ('serialnumber', models.CharField(blank=True, max_length=96, verbose_name='\u5e8f\u5217\u53f7')),
                ('description', models.CharField(blank=True, max_length=5000, verbose_name='\u63cf\u8ff0')),
                ('status', models.CharField(blank=True, default='000', max_length=3, verbose_name='\u72b6\u6001')),
                ('installtime', models.DateField(blank=True, null=True, verbose_name='\u5b89\u88c5\u65e5\u671f')),
                ('is_monitoring', models.BooleanField(default=True)),
                ('pandianstatus', models.IntegerField(choices=[(1, '\u5df2\u76d8\u70b9'), (2, '\u5f85\u76d8\u70b9'), (3, '\u5176\u4ed6')], default=1, verbose_name='\u76d8\u70b9\u72b6\u6001')),
                ('pandiantime', models.DateField(blank=True, null=True, verbose_name='\u6700\u65b0\u4e00\u6b21\u76d8\u70b9\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907',
                'verbose_name_plural': '\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='Device2MepSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'devicemanage_device2mepsystem',
                'verbose_name': '\u8bbe\u5907',
                'verbose_name_plural': '\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='DeviceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=96, verbose_name='\u7c7b\u578b\u540d\u79f0')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=96, verbose_name='\u7c7b\u578b\u540d\u79f0')),
                ('assettype', models.CharField(blank=True, max_length=96, verbose_name='\u8d44\u4ea7\u7c7b\u578b')),
                ('dtype', models.CharField(blank=True, max_length=96, verbose_name='\u578b\u53f7')),
                ('dformat', models.CharField(blank=True, max_length=96, verbose_name='\u89c4\u683c')),
                ('supplier', models.CharField(blank=True, max_length=96, verbose_name='\u751f\u4ea7\u5382\u5bb6')),
                ('warrantydescription', models.CharField(blank=True, max_length=96, verbose_name='\u8d28\u4fdd\u63cf\u8ff0')),
                ('exceptedlife', models.IntegerField(blank=True, verbose_name='\u9884\u8ba1\u4f7f\u7528\u5e74\u9650')),
                ('exceptedlifeunit', models.CharField(blank=True, max_length=10, verbose_name='\u9884\u8ba1\u4f7f\u7528\u5e74\u9650\u5355\u4f4d')),
                ('replacementcost', models.CharField(blank=True, max_length=96, verbose_name='\u7f6e\u6362\u91d1\u989d')),
                ('material', models.CharField(blank=True, max_length=96, verbose_name='\u6750\u6599')),
                ('shape', models.CharField(blank=True, max_length=96, verbose_name='\u5f62\u72b6')),
                ('size', models.CharField(blank=True, max_length=96, verbose_name='\u5c3a\u5bf8')),
                ('nominallength', models.CharField(blank=True, max_length=96, verbose_name='\u6807\u79f0\u957f\u5ea6')),
                ('nominalwidth', models.CharField(blank=True, max_length=96, verbose_name='\u6807\u79f0\u5bbd\u5ea6')),
                ('nominalheight', models.CharField(blank=True, max_length=96, verbose_name='\u6807\u79f0\u9ad8\u5ea6')),
                ('classification', models.CharField(blank=True, max_length=96, verbose_name='\u5206\u7c7b\u6761\u76ee')),
                ('manufacturer', models.CharField(blank=True, max_length=96, verbose_name='\u6240\u5c5e\u7cfb\u7edf\u7c7b\u578b')),
            ],
            options={
                'db_table': 'DeviceManage_DeviceType',
                'verbose_name': '\u8bbe\u5907\u7c7b\u578b',
                'verbose_name_plural': '\u8bbe\u5907\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='MepSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=96, verbose_name='\u7cfb\u7edf\u540d\u79f0')),
            ],
            options={
                'db_table': 'DeviceManage_MepSystem',
                'verbose_name': '\u673a\u7535\u7cfb\u7edf',
                'verbose_name_plural': '\u673a\u7535\u7cfb\u7edf',
            },
        ),
        migrations.CreateModel(
            name='MepSystemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=96, verbose_name='\u7cfb\u7edf\u7c7b\u578b\u540d\u79f0')),
                ('RedatedBAName', models.CharField(blank=True, max_length=96, verbose_name='BA\u5bf9\u5e94\u540d\u79f0')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u6a21\u578b\u7b80\u4ecb')),
                ('color_code', models.CharField(default='#ff0000', max_length=8, verbose_name='\u6a21\u578b\u90e8\u95e8\u6e32\u67d3')),
            ],
            options={
                'db_table': 'DeviceManage_MepSystemType',
                'verbose_name': '\u673a\u7535\u7cfb\u7edf\u7c7b\u578b',
                'verbose_name_plural': '\u673a\u7535\u7cfb\u7edf\u7c7b\u578b',
            },
        ),
    ]
