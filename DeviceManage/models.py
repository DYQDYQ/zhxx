# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

# Create your models here.

class MepSystemType(models.Model):
    '''机电系统类型'''
    name = models.CharField(max_length=96, blank=True,verbose_name='系统类型名称')
    classification = models.ForeignKey('ModelManage.RoomclassFication',verbose_name='分类条目',null=True,blank=True)
    # major = models.ForeignKey(Major,verbose_name='专业',null=True,blank=True)
    RedatedBAName = models.CharField(max_length=96, blank=True,verbose_name='BA对应名称')
    parentSystem = models.ForeignKey('self',verbose_name='父系统类型',blank=True,null=True)
    description = models.TextField(verbose_name='模型简介',blank=True,null=True)
    color_code = models.CharField(max_length=8,verbose_name=u'模型部门渲染',default='#ff0000')

    class Meta:
        verbose_name = '机电系统类型'
        verbose_name_plural = '机电系统类型'
        db_table = 'DeviceManage_MepSystemType'

    def __str__(self):
        return self.name


class DeviceCategory(models.Model):
    '''设备大类型'''
    name = models.CharField(max_length=96, blank=True,verbose_name='类型名称')

    
    def __str__(self):
        return self.name

class MepSystem(models.Model):
    '''机电系统'''
    name = models.CharField(max_length=96, blank=True,verbose_name='系统名称')
    systemType = models.ForeignKey(MepSystemType,verbose_name='系统类型',null=True,blank=True,related_name="mepsystem")
    # major = models.ForeignKey(Major,verbose_name='专业')
    # asset = models.ForeignKey('AssetManage.Asset',verbose_name=u'资产id',null=True)


    def __str__(self):
        return self.name

    def devices(self):
        return Device.objects.filter(mepsystem=self).count()
    class Meta:
        verbose_name = '机电系统'
        verbose_name_plural = '机电系统'
        db_table = 'DeviceManage_MepSystem'


class DeviceType(models.Model):
    '''设备类型'''
    name = models.CharField(max_length=96, blank=True,verbose_name='类型名称')
    assettype = models.CharField(max_length=96, blank=True,verbose_name='资产类型')
    dtype = models.CharField(max_length=96, blank=True,verbose_name='型号')
    dformat = models.CharField(max_length=96, blank=True,verbose_name='规格')
    manufacturer = models.CharField(max_length=96, blank=True,verbose_name='供应商')
    supplier = models.CharField(max_length=96, blank=True,verbose_name='生产厂家')
    warrantydescription = models.CharField(max_length=96, blank=True,verbose_name='质保描述')
    exceptedlife = models.IntegerField(blank=True,verbose_name='预计使用年限')
    exceptedlifeunit= models.CharField(max_length=10, blank=True,verbose_name='预计使用年限单位')
    replacementcost = models.CharField(max_length=96, blank=True,verbose_name='置换金额')
    material = models.CharField(max_length=96, blank=True,verbose_name='材料')
    shape = models.CharField(max_length=96, blank=True,verbose_name='形状')
    size = models.CharField(max_length=96, blank=True,verbose_name='尺寸')
    nominallength = models.CharField(max_length=96, blank=True,verbose_name='标称长度')
    nominalwidth = models.CharField(max_length=96, blank=True,verbose_name='标称宽度')
    nominalheight = models.CharField(max_length=96, blank=True,verbose_name='标称高度')
    # major = models.ForeignKey(Major, blank=True,verbose_name='专业')
    classification = models.CharField(max_length=96, blank=True,verbose_name='分类条目')
    manufacturer = models.CharField(max_length=96, blank=True,verbose_name='所属系统类型')
    # mepsystem = models.ForeignKey(MepSystem,verbose_name='系统',blank=True,null=True)
    mepsystemtype = models.ForeignKey(MepSystemType,verbose_name='系统类型',blank=True,null=True,related_name="DeviceType")
    modelurl = models.ForeignKey('ModelManage.ModelUrl',verbose_name='精细模型链接',blank=True,null=True)
    device_category = models.ForeignKey(DeviceCategory,verbose_name='设备大类型',blank=True,null=True,related_name="DeviceType")
    parent = models.ForeignKey('self',verbose_name='父节点',null=True,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备类型'
        verbose_name_plural = '设备类型'
        db_table = 'DeviceManage_DeviceType'


class Device(models.Model):
    '''设备'''
    CHOICES = (
        (1, '已盘点'),
        (2, '待盘点'),
        (3, '其他'),
    )
    devicetype = models.ForeignKey(DeviceType,blank=True,null=True,related_name="Device",verbose_name='设备类型')
    # mepsystem = models.ForeignKey(MepSystem,blank=True,null=True)
    room = models.ForeignKey('SpaceManage.SpaceRoom',blank=True,null=True,related_name="deviceF")
    # 楼宇-楼层-房间号-设备类型编号-设备编号
    code = models.CharField(max_length=96,null=True, blank=True,verbose_name='二维码')
    serialnumber = models.CharField(max_length=96, blank=True,verbose_name='序列号')
    description = models.CharField(max_length=5000, blank=True,verbose_name='描述')
    model = models.ForeignKey('ModelManage.PrecastBeam',blank=True,null=True,related_name='Device')
    mepsystem= models.ManyToManyField(MepSystem,verbose_name='设备系统',related_name="mepsystemF",through='Device2MepSystem')
    status = models.CharField(max_length=3, blank=True,verbose_name='状态',default='000')# 000 111 维修，维保，预警
    installtime = models.DateField(blank=True,null=True,verbose_name='安装日期')
    # user = models.ForeignKey('User.User',verbose_name='运维负责人',blank=True,null=True)
    is_monitoring = models.BooleanField(default=True)#区分是否为带监测数据的重要设备。
    # asset = models.ForeignKey('AssetManage.Asset',verbose_name=u'资产id',null=True)
    pandianstatus = models.IntegerField(default=1,verbose_name='盘点状态',choices=CHOICES)
    pandiantime = models.DateField(blank=True,null=True,verbose_name='最新一次盘点时间')
    # DeviceStatus = models.ForeignKey('DeviceStatus',blank=True,null=True)

    def __str__(self):
        if self.code:
            return self.devicetype.name +'-'+ self.code
        else:
            return '--'

    class Meta:
        verbose_name = "设备"
        verbose_name_plural = verbose_name

class Device2MepSystem(models.Model):
    device = models.ForeignKey(Device,blank=True,null=True)
    mepsystem = models.ForeignKey(MepSystem,blank=True,null=True)
    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'
        db_table = 'devicemanage_device2mepsystem'