import os
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def static_file_exists(file_path):
    static_path = os.path.join(settings.STATIC_ROOT, file_path)
    return os.path.exists(static_path)