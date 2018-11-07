# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from rest_framework import routers
from SpaceManage.views import * 
router = routers.DefaultRouter()


router.register(r'room', RoomSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]