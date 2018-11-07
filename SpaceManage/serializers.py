# -*- coding: utf-8 -*-
from rest_framework import serializers

from django.db.models import Q
from .models import *

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceFloor
        fields = "__all__"
        # fields = ("name",)


class RoomSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    floor_name = serializers.ReadOnlyField(required=False,source='floorname')
    # floor = FloorSerializer()
    department_name = serializers.ReadOnlyField(required=False,source='departmentname')
    category_name = serializers.ReadOnlyField(required=False,source='categoryname')
    floorid = serializers.ReadOnlyField(required=False,source='floor_id')

    def validate_netarea(self, netarea):
        print '--------'
        print self
        if netarea > self.grossarea:
            raise serializers.ValidationError("实用面积大于设计面积")

    class Meta:
       model = SpaceRoom
       fields = "__all__"