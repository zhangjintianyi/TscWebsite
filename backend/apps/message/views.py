from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from backend.apps.message.models import Message
from backend.apps.message.serilalizers import MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class Pagination(PageNumberPagination):
    """
    分页类，规定分页情况
    """
    page_size = 5
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
    def create(self, request, *args, **kwargs):
        job_num = request.data["writer"]
        user = User.objects.get(job_num=job_num)
        message = Message.objects.create(writer=user, title=request.data["title"], content=request.data["content"],
                                         version=request.data["version"])
        for reminder_job_num in request.data["reminders"]:
            reminder = User.objects.get(job_num=reminder_job_num)
            message.reminders.add(reminder)
        serializer = MessageSerializer(instance=message)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.reminders.clear()
        for reminder_job_num in request.data["reminders"]:
            reminder = User.objects.get(job_num=reminder_job_num)
            instance.reminders.add(reminder)
        serializer = MessageSerializer(instance=instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
