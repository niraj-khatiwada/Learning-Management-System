import os
from django import template
register = template.Library()

@register.filter
def extension(value):
    return os.path.basename(value.file.name.split('.')[-1])