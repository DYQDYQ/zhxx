# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User as DjangoUser


class Address(models.Model):
    """docstring for address"""
    city = models.CharField(max_length=64,verbose_name=u'城市',null=True,blank=True)
    region = models.CharField(max_length=64,verbose_name=u'区域',null=True,blank=True)
    street = models.CharField(max_length=64,verbose_name=u'街道',null=True,blank=True)
    code = models.CharField(max_length=64,verbose_name=u'编号',null=True,blank=True)
    class Meta:
        db_table = 'usermanagement_address'
        verbose_name = '地址'
        verbose_name_plural = '地址'

class department(models.Model):
    '''部门'''
    name = models.CharField(max_length=64,verbose_name=u'部门名称')
    telephone = models.IntegerField(blank=True, verbose_name=u'方式',null=True)
    # address = models.CharField(max_length=64,verbose_name=u'办公地址',blank=True,null=True)
    address = models.ForeignKey(Address,verbose_name=u'办公地址',blank=True,null=True)
    color_code = models.CharField(max_length=8,verbose_name=u'模型部门渲染',default='#ff0000')
    # menu = models.ManyToManyField(Menu,blank=True,verbose_name='部门可见菜单列表')
    # auth = models.ManyToManyField('UserAuth',blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'usermanagement_department'
        verbose_name = '部门'
        verbose_name_plural = '部门'

class User(models.Model):
    '''用户自定义字段'''
    auth_user = models.OneToOneField(DjangoUser,related_name='User', blank=True, null=True)
    truename = models.CharField(max_length=16, default='', blank=True,verbose_name=u'昵称')
    contract = models.CharField(max_length=16, default='', blank=True,verbose_name=u'电话')
    department=models.ForeignKey(department,verbose_name=u'部门ID', blank=True,null=True)
    # role=models.ForeignKey(UserRole,verbose_name=u'角色', blank=True,null=True)
    def __str__(self):
        return self.truename

    class Meta:
        db_table = 'usermanagement_user_profile'
        verbose_name = '电话与昵称'
        verbose_name_plural = '电话与昵称'