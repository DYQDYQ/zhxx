# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from Nuser.models import User, department

# Create your models here.

class RoomAssignment(models.Model):
    """
    空间分配
    """
    user = models.ForeignKey(User, related_name="user_id", null=True, blank=True, verbose_name="负责人ID")
    assignment_time = models.DateTimeField(null=True, blank=True, verbose_name="分配时间")
    fenpei = models.ForeignKey(User, related_name="fenpei_id", null=True, blank=True, verbose_name="分配人ID")
    begin_time = models.DateTimeField(null=True, blank=True, verbose_name="开始时间")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="结束时间")
    remark = models.TextField(default="", verbose_name="备注")

    class Meta:
        verbose_name = '空间分配'
        verbose_name_plural = verbose_name


class CategoryRoom(models.Model):
    """
    房间类型
    """
    renderstyle = models.CharField(default="", max_length=30, verbose_name="渲染样式")
    name = models.CharField(default="", max_length=30, verbose_name="类型名称")

    class Meta:
        verbose_name = "房间类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class SpaceBuilding(models.Model):

    """
    教学楼
    """
    name = models.CharField(default="", max_length=30, verbose_name="学校名", help_text='学校名')

    class Meta:
        verbose_name = '教学楼'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

class SpaceFloor(models.Model):
    """
    楼层
    """
    name = models.CharField(default="", max_length=30, verbose_name="楼层")
    level = models.CharField(default="", max_length=64, verbose_name=u'标高')
    sign = models.CharField(default="",max_length=64,verbose_name=u'标记')
    facility = models.ForeignKey(SpaceBuilding, null=True, blank=True, verbose_name="所属教学楼")
    coefficient = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u'系数',null=True,blank=True)
    description = models.TextField(verbose_name=u'楼层描述',default="")
    area = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'面积',null=True,blank=True)
    model = models.ForeignKey('ModelManage.PrecastBeam',blank=True,null=True,related_name='Floor')

    class Meta:
        verbose_name = '楼层'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class SpaceRoom(models.Model):
    """
    房间
    """
    room_number = models.IntegerField(default=0, verbose_name="房间号")
    category = models.ForeignKey(CategoryRoom, null=True, blank=True, verbose_name="房间类型")
    department = models.ForeignKey(department, null=True, blank=True, verbose_name="使用部门ID")
    grossarea = models.IntegerField(default=0, verbose_name="建筑面积")
    netarea = models.CharField(default=0, max_length = 30, verbose_name="实际计算面积")
    remark = models.TextField(default="", verbose_name="备注")
    floor = models.ForeignKey(SpaceFloor, null=True, blank=True, verbose_name='楼层ID')
    purpose = models.TextField(default="", verbose_name="房间用途")
    asset = models.TextField(default="", verbose_name="资产")
    boundary = models.CharField(default="",max_length=30, verbose_name="房间边界")
    assignment = models.ForeignKey(RoomAssignment, null=True, blank=True, verbose_name="空间分配")

    def floorname(self):
        if self.floor:
            return self.floor.name
        else:
            return '--'

    def departmentname(self):
        if self.department:
            return self.department.name
        else:
            return '--'
    
    def categoryname(self):
        if self.category:
            return self.category.name
        else:
            return '--'        
     
    class Meta:
        verbose_name = "房间"
        verbose_name_plural = verbose_name

class SpaceZone(models.Model):
    """
    分区
    """
    name = models.CharField(default="", max_length=30, verbose_name="分区名称")
    remark = models.TextField(default="", verbose_name="备注")
    parentSpace = models.ForeignKey("self", null=True, blank=True, verbose_name="父分区级别", help_text="父目录",
                                        related_name="sub_cat")
    rooms = models.ManyToManyField(SpaceRoom, blank=True,related_name = 'Zone')
    class Meta:
        verbose_name = "分区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SpaceIbeacon(models.Model):
    """
    空间定位设备
    """
    ibeacon_UUID = models.CharField(default="", max_length=30 , verbose_name="设备唯一标识")
    ibeacon_major = models.CharField(default="", max_length=30 , verbose_name="自定义标识")
    ibeacon_minor = models.CharField(default="", max_length=30 , verbose_name="自定义标识符")
    room = models.ForeignKey(SpaceRoom, null=True, blank=True, verbose_name='关联房间')
    device = models.ForeignKey('DeviceManage.Device', null=True, blank=True, verbose_name='关联设备')
    msg_template = models.TextField(default="", verbose_name='信息模板')

    class Meta:
        verbose_name = "空间定位设备"
        verbose_name_plural = verbose_name

