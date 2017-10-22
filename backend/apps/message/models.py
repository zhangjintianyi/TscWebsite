from datetime import datetime

from django.db import models

from backend.apps.users.models import UserProfile


# Create your models here.

class Message(models.Model):
    writer = models.ForeignKey(UserProfile, related_name="write_messages", verbose_name="发布人")
    title = models.CharField(max_length=50, verbose_name="标题")
    content = models.TextField(max_length=200, null=True, blank=True, verbose_name="内容")
    version = models.CharField(max_length=20, null=True, blank=True, verbose_name="使用版本")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    reminders = models.ManyToManyField(UserProfile, related_name="remind_messages", verbose_name="重点提醒人")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{writer}: {title}".format(writer=self.writer, title=self.title)