from django import template
from index.models import Notification
import os
register = template.Library()

@register.filter(name = 'filename')
def filename(value):
    try:
        note = Notification.objects.get(file_attached=value)
        return os.path.split(note.file_attached.name)[-1]
    except:
        return none

@register.filter(name = 'filelink')
def filelink(value):
    try:
        note = Notification.objects.get(file_attached=value)
        return 'http://127.0.0.1:8000/download/?file={0}'.format(note.file_attached.name)
    except:
        return None
