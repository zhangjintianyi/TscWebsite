from rest_framework import serializers

from backend.apps.message.models import Message
from backend.apps.users.serilalizers import UserDetailSerializer


class MessageSerializer(serializers.ModelSerializer):
    writer = UserDetailSerializer(read_only=True)
    reminders = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
