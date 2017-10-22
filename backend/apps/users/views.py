from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import mixins
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.parsers import FileUploadParser
from TscWebsite.settings import MEDIA_ROOT

from backend.apps.users.serilalizers import UserDetailSerializer, UserRegSerializer

User = get_user_model()


# Create your views here.
class Pagination(PageNumberPagination):
    """
    分页类，规定分页情况
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(job_num=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = "job_num"

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegSerializer
        if self.action == "retrieve":
            return UserDetailSerializer
        return UserDetailSerializer

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(job_num=request.data["job_num"])
            payload = jwt_payload_handler(user)
            res = dict(request.data)
            res.pop("password")
            res["token"] = jwt_encode_handler(payload)
            return Response(res)
        except User.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            user = self.perform_create(serializer)
            re_dict = serializer.data
            payload = jwt_payload_handler(user)
            re_dict["token"] = jwt_encode_handler(payload)
            headers = self.get_success_headers(serializer.data)
            return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()

    def perform_update(self, serializer):
        return serializer.save()


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        if (self.size_verify(file_obj.size)):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(job_num=self.request.user.job_num)
        user.avatar = file_obj.name
        user.save()
        if file_obj:
            photo_name = 'avatar_%s' % (request.user.job_num) + '.jpg'
            photo_path = MEDIA_ROOT + "/avatar/" + photo_name
            with open(photo_path, "wb+") as f:
                # for chunk in file_obj.chunks():
                f.write(file_obj.read())

        return Response(status=201)

    def size_verify(self, size):
        return (size / 1024 / 1024) > 2
