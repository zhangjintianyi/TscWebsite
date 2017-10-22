from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from backend.apps.message.models import Message
from backend.apps.message.serilalizers import MessageSerializer


# Create your views here.
class Pagination(PageNumberPagination):
    """
    分页类，规定分页情况
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class MessageViewSet(viewsets.ModelViewSet):
    """
    Message视图
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('writer', 'title', 'content', 'version', 'add_time', 'reminders')
