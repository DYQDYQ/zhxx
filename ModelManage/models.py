# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from SpaceManage.models import SpaceFloor, SpaceRoom, SpaceZone, SpaceBuilding

# Create your models here.

class PBStatus(models.Model):
    '''构件状态表'''
    name=models.CharField(max_length=60,verbose_name='状态名称')
    class Meta:
        verbose_name = '构件状态表'
        verbose_name_plural = verbose_name
        db_table = 'ModelManage_pbstatus'

class PBMaterial(models.Model):
    '''构件材料表'''
    # MATERIAL_TYPE_CHOICES = (
    #     ('钢材', '钢材'),
    #     ('混泥土', '混泥土'),
    #     ('钢筋', '钢筋'),
    # )
    name = models.CharField(max_length=20,verbose_name='类型')
    specification = models.CharField(max_length=30,verbose_name='规格',null=True,blank=True)
    size = models.CharField(max_length=30,verbose_name='材料尺寸',null=True,blank=True)
    class Meta:
        verbose_name = '构件材料表'
        verbose_name_plural = verbose_name
        db_table = 'ModelManage_pbmaterial'


class PBType(models.Model):
    '''构件类型表'''
    name = models.CharField(max_length=60,verbose_name='名称')
    material = models.ForeignKey(PBMaterial,verbose_name='材料',null=True,blank=True)
    # major = models.ForeignKey(Major,verbose_name='专业',null=True,blank=True)
    classfication_code = models.CharField(max_length=64,verbose_name='分类编码',null=True,blank=True)
    sign = models.CharField(max_length=60,verbose_name='标记',null=True,blank=True)
    familyname = models.CharField(max_length=60,verbose_name='族名称',null=True,blank=True)
    description = models.CharField(max_length=200,verbose_name='描述',null=True,blank=True)
    isprebuilt = models.BooleanField(verbose_name='是否预制',default=True)
    # manufacturer = models.ForeignKey('User.Company', verbose_name='生产厂家',null=True,blank=True)
    class Meta:
        verbose_name = '构件类型表'
        verbose_name_plural = verbose_name
        db_table = 'ModelManage_pbtype'

class PbGroup(models.Model):
    '''构件分组表'''
    number = models.CharField(max_length=64,verbose_name='编号')
    name = models.CharField(max_length=64,verbose_name='组名')
    pbtype = models.ForeignKey(PBType, verbose_name='类型',null=True,blank=True)
    zone = models.ForeignKey(SpaceZone, verbose_name='所属分区',null=True,blank=True)
    class Meta:
        verbose_name = '构件分组表'
        verbose_name_plural = verbose_name
        db_table = 'ModelManage_pbgroup'



class RoomclassFication(models.Model):
    '''空间知识库'''
    pbtype = models.ForeignKey(PBType,verbose_name=u'构件类型',null=True)
    name = models.CharField(max_length=64,verbose_name=u'分类名称')
    aliasName = models.CharField(max_length=64,verbose_name=u'别称')
    code = models.CharField(max_length=64,verbose_name=u'分类编码')
    parent = models.ForeignKey('self',verbose_name='父分类')
    relCbimCode = models.CharField(max_length=64,verbose_name=u'对应国家分类体系')
    

    class Meta:
        verbose_name = '空间知识库'
        verbose_name_plural = verbose_name
        db_table = 'SpaceManage_Knowledge_RoomclassFication'

    def __str__(self):
        return self.code

class PrecastBeam(models.Model):
    '''构件表'''
    guid=models.CharField(max_length=64,unique=True,verbose_name='GUID')
    revitfilename=models.CharField(max_length=60,verbose_name='Revit文件名',null=True,blank=True)
    elementid=models.CharField(max_length=60,verbose_name='ElementID',null=True,blank=True)
    systemlmvdbid=models.IntegerField(verbose_name='系统lmvdbid',null=True,blank=True)
    floorlmvdbid=models.IntegerField(verbose_name='分层lmvdbid',null=True,blank=True)
    systematic_diagram_lmvdbid=models.IntegerField(verbose_name='机电系统图',null=True,blank=True)
    parkdbid=models.IntegerField(verbose_name='园区模型dbid',null=True,blank=True)
    detaildbid=models.IntegerField(verbose_name='精细模型dbid',null=True,blank=True)
    number=models.CharField(max_length=64,verbose_name='编号',null=True,blank=True)
    pbtype=models.ForeignKey(PBType,verbose_name='构件类型',null=True,blank=True)
    curstatus=models.ForeignKey(PBStatus,null=True,blank=True,verbose_name='当前状态')
    curstatustime=models.DateTimeField(verbose_name='当前状态时间')
    weight=models.FloatField(verbose_name='重量',null=True,blank=True)
    volume=models.FloatField(verbose_name='体积',null=True,blank=True)
    width=models.FloatField(verbose_name='宽度',null=True,blank=True)
    height=models.FloatField(verbose_name='高度',null=True,blank=True)
    length=models.FloatField(verbose_name='长度',null=True,blank=True)
    sign=models.CharField(max_length=60,verbose_name='标记',null=True,blank=True)
    floor=models.ForeignKey(SpaceFloor,verbose_name='楼层',null=True,blank=True)
    proom=models.ForeignKey(SpaceRoom,verbose_name='房间',null=True,blank=True)
    mepsystem=models.ForeignKey('DeviceManage.MepSystem',verbose_name='系统',null=True,blank=True)
    pbposition_x=models.CharField(max_length=64,unique=True,verbose_name='构件位置x',null=True,blank=True)
    pbposition_y=models.CharField(max_length=64,unique=True,verbose_name='构件位置y',null=True,blank=True)
    pbposition_z=models.CharField(max_length=64,unique=True,verbose_name='构件位置z',null=True,blank=True)
    pbpostion = models.CharField(max_length=64,unique=True,verbose_name='构件位置',null=True,blank=True)
    # facility=models.ForeignKey(Room,verbose_name='关联设备ID',null=True)
    description=models.CharField(max_length=4000,verbose_name='描述',blank=True,null=True)
    drawnumber=models.CharField(max_length=60,verbose_name='图纸编号',blank=True,null=True)
    # task=models.ForeignKey("ProjectTask",verbose_name='所属任务',null=True,blank=True)
    pbpostion=models.CharField(max_length=64,blank=True,null=True,verbose_name='位置字符串')
    parentguid=models.CharField(max_length=64,blank=True,null=True,verbose_name='父构件GUID')
    # asset = models.ForeignKey('AssetManage.Asset',verbose_name=u'资产id',null=True)
    # curfactoryposition=models.ForeignKey(FactoryPosition,verbose_name='当前场地仓位',null=True,blank=True)

    class Meta:
        verbose_name = "构建表"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        if self.floorlmvdbid:
            return u'构件'+ str(self.floorlmvdbid)+str(self.systemlmvdbid)
        return u'构件'
        

class PbGroupRelation(models.Model):
    '''构件与分组关系'''
    pbgroup = models.ForeignKey(PbGroup,null=True,blank=True)
    pb = models.ForeignKey(PrecastBeam,null=True,blank=True)
    class Meta:
        verbose_name = "构件与分组关系"
        verbose_name_plural = verbose_name
        db_table = 'ModelManage_pbgrouprelation'



class ModelUrl(models.Model):
    """
    模型表
    """
    CHOICES = (
        ('floor', 'floor'),
        ('mepsystemtype', 'mepsystemtype'),
        ('space', 'space'),
        ('device', 'device'),
        ('yuanqu', 'yuanqu'),
        ('jifang', 'jifang'),
        ('camera', 'camera'),
    )
    urltype1 = models.CharField(max_length=256,verbose_name=u'模型类型',choices=CHOICES,null=True)#楼层，系统
    urlid = models.IntegerField()
    facility = models.ForeignKey(SpaceBuilding,null=True)
    # major = models.ForeignKey('User.Major',null=True)
    url = models.CharField(max_length=256,verbose_name=u'模型地址',null=True)
    nexturl = models.CharField(max_length=256,verbose_name=u'双模型第二个模型地址',null=True)
    models = models.ManyToManyField(PrecastBeam, through='ModelUrl2Model',related_name='ModelUrl')

    class Meta:
        verbose_name = "模型表"
        verbose_name_plural = verbose_name

class ModelUrl2Model(models.Model):
    """docstring for ModelUrl2Model"""
    model = models.ForeignKey(PrecastBeam,related_name='ModelUrl2Model')
    modelurl = models.ForeignKey(ModelUrl)
    dbid = models.IntegerField(null=True,blank=True,verbose_name=u'构件forgedbid')
    class Meta:
        db_table = 'ModelManage_ModelUrl2Model'

