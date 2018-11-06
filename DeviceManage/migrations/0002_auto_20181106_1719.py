# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-11-06 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SpaceManage', '0001_initial'),
        ('DeviceManage', '0001_initial'),
        ('ModelManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mepsystemtype',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelManage.RoomclassFication', verbose_name='\u5206\u7c7b\u6761\u76ee'),
        ),
        migrations.AddField(
            model_name='mepsystemtype',
            name='parentSystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DeviceManage.MepSystemType', verbose_name='\u7236\u7cfb\u7edf\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='mepsystem',
            name='systemType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mepsystem', to='DeviceManage.MepSystemType', verbose_name='\u7cfb\u7edf\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='device_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DeviceType', to='DeviceManage.DeviceCategory', verbose_name='\u8bbe\u5907\u5927\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='mepsystemtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DeviceType', to='DeviceManage.MepSystemType', verbose_name='\u7cfb\u7edf\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='modelurl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ModelManage.ModelUrl', verbose_name='\u7cbe\u7ec6\u6a21\u578b\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DeviceManage.DeviceType', verbose_name='\u7236\u8282\u70b9'),
        ),
        migrations.AddField(
            model_name='device2mepsystem',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DeviceManage.Device'),
        ),
        migrations.AddField(
            model_name='device2mepsystem',
            name='mepsystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DeviceManage.MepSystem'),
        ),
        migrations.AddField(
            model_name='device',
            name='devicetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Device', to='DeviceManage.DeviceType', verbose_name='\u8bbe\u5907\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='device',
            name='mepsystem',
            field=models.ManyToManyField(related_name='mepsystemF', through='DeviceManage.Device2MepSystem', to='DeviceManage.MepSystem', verbose_name='\u8bbe\u5907\u7cfb\u7edf'),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Device', to='ModelManage.PrecastBeam'),
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deviceF', to='SpaceManage.SpaceRoom'),
        ),
    ]