from backend.extra_apps import xadmin
from backend.apps.message.models import Message


class MessageAdmin(object):
    list_display = ['writer', 'title', 'content', 'version', 'add_time', 'reminders']
    search_fields = ['writer', 'title', 'version', 'add_time', 'reminder']


xadmin.site.register(Message, MessageAdmin)
