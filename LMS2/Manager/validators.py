
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
import string

def validate_name(name):
    for i in name:
        if not i in string.ascii_letters and not i in string.whitespace:
            raise ValidationError(gettext_lazy('Name is not valid. Use only "A-Z a-"'))
    return name

def validate_designation(designation):
    for i in designation:
        if not i in string.ascii_letters and not i in "," and not i in string.whitespace:
            raise ValidationError(gettext_lazy('Enter a valid address'))
    return designation