from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


import string

def validate_name(name):
    for i in name:
        if not i in string.ascii_letters and not i in string.whitespace:
            raise ValidationError(gettext_lazy("Name is not valid"))
    return name

def validate_designation(designation):
    for i in designation:
        if not i in string.ascii_letters and not i in string.whitespace and not i in ",":
            raise ValidationError(gettext_lazy("Address is not valid")) 
    return designation