# -*- coding: utf-8 -*-

import rest_framework_filters as filters
from django.db.models import Q

from .models import *

class RoomFilter(filters.FilterSet):
    class Meta:
        model = SpaceRoom
        fields = {
            'category':['exact', 'in'],
            'department':['exact', 'in','isnull'],
            'floor':['exact','in'],
            'id':['in'],
            'floor__facility':['exact', 'in']
        }