from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    job_num = serializers.CharField(required=True, label="工号", help_text="请填写工号，型如：z18861",
                                    validators=[UniqueValidator(queryset=User.objects.all(), message="工号已存在")])
    username = serializers.CharField(required=True, allow_null=True, label="名字", help_text="请输入您的名字，例如：张三 李四", )
    password = serializers.CharField(required=True, label="密码", help_text="请输入密码密码", write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = User
        fields = ("job_num", "username", "password")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("job_num", "username", "email", "mobile", "phone", "avatar")
