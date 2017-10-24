"""TscWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from TscWebsite.settings import MEDIA_ROOT
from backend.extra_apps import xadmin
from backend.apps.tsc.views import MSOViewSet, TSCViewSet, DBSViewSet
from backend.apps.users.views import UserViewSet, FileUploadView
from backend.apps.message.views import MessageViewSet

router = DefaultRouter()
router.register(r"mso", MSOViewSet, base_name="mso")
router.register(r"tsc", TSCViewSet, base_name="tsc")
router.register(r"dbs", DBSViewSet, base_name="dbs")
router.register(r"users", UserViewSet, base_name="users")
router.register(r"messages", MessageViewSet, base_name="messages")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^upload/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
   url(r'^upload/avatar/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    url(r'^api/v1/', include(router.urls)),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
