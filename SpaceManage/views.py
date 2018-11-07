# -*- coding: utf-8 -*-

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import *
from .serializers import RoomSerializer
from .filters import RoomFilter

# Create your views here.

class NowPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class RoomSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    房间列表页
    """
    queryset = SpaceRoom.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('room_number', 'category', 'department', 'purpose')
    filter_class = RoomFilter
    ordering_fields = ('room_number', 'category', 'department', 'purpose')
    pagination_class = NowPagination