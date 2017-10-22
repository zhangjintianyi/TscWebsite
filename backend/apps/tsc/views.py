from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from backend.apps.tsc.models import MSO, TSC, DBS
from backend.apps.tsc.serilalizers import MSOSerializer, TSCSerializer, DBSSerializer


# Create your views here.

class Pagination(PageNumberPagination):
    """
    分页类，规定分页情况
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class MSOViewSet(viewsets.ModelViewSet):
    """
    MSO视图
    """
    queryset = MSO.objects.all()
    serializer_class = MSOSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('ip', 'department', 'version', 'principal')


class TSCViewSet(viewsets.ModelViewSet):
    """
    TSC视图
    """
    queryset = TSC.objects.all()
    serializer_class = TSCSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('mso', 'ip', 'department', 'version', 'principal', 'tsc_type')


class DBSViewSet(viewsets.ModelViewSet):
    """
    DBS视图
    """
    queryset = DBS.objects.all()
    serializer_class = DBSSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('mso', 'ip', 'department', 'version', 'principal', 'dbs_type')
